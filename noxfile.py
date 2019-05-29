import nox

# Note: This causes `nox -l` to omit other sessions
# Fixed in https://github.com/theacodes/nox/pull/185, pending release
nox.options.sessions = ['test']


def get_envname(python_version):
    """Return the name a tox default environment"""
    return f"py{python_version.replace('.', '')}"


def get_suffix(python_version):
    """Return a requirements file suffix based on Python version"""
    envname = get_envname(python_version)
    # Maintain compatibility with existing tooling
    return '' if envname == 'py27' else f"-{envname}"


@nox.session(python=['2.7', '3.7'])
def requirements(session):
    session.install('pip-tools')

    suffix = get_suffix(session.python)
    base_txt = f"base{suffix}.txt"
    dev_txt = f"dev{suffix}.txt"

    session.chdir('requirements')
    session.run('pip-compile', '-o', base_txt, 'base.in')
    session.run('pip-compile', '-o', dev_txt, base_txt, 'dev.in')


@nox.session(python=['2.7', '3.7'])
def test(session):
    suffix = get_suffix(session.python)
    session.install('-r', f"requirements/dev{suffix}.txt")

    command = session.posargs or ['pip', 'freeze']
    session.run(*command)
