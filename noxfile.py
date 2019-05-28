import shutil
import nox

# Note: This causes `nox -l` to omit other sessions
# Fixed in https://github.com/theacodes/nox/pull/185, pending release
nox.options.sessions = ['test']


def get_envname(python_version):
    """Return the name a tox default environment"""
    return f"py{python_version.replace('.', '')}"


@nox.session(python=['2.7', '3.7'])
def requirements(session):
    session.install('pip-tools')

    envname = get_envname(session.python)
    base_txt = f"base-{envname}.txt"
    dev_txt = f"dev-{envname}.txt"

    session.chdir('requirements')
    session.run('pip-compile', '-o', base_txt, 'base.in')
    session.run('pip-compile', '-o', dev_txt, base_txt, 'dev.in')

    # Maintain compatibility with existing tooling
    if session.python == '2.7':
        shutil.copy(base_txt, 'base.txt')
        shutil.copy(dev_txt, 'dev.txt')


@nox.session(python=['2.7', '3.7'])
def test(session):
    envname = get_envname(session.python)
    session.install('-r', f"requirements/dev-{envname}.txt")

    command = session.posargs or ['pip', 'freeze']
    session.run(*command)
