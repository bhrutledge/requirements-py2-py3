import nox


def get_envname(python_version):
    """Return the name a tox default environment"""
    return f"py{python_version.replace('.', '')}"


@nox.session(python=['2.7', '3.7'])
def requirements(session):
    envname = get_envname(session.python)

    session.install('pip-tools')
    session.chdir('requirements')

    session.run(
        'pip-compile',
        '-o', f"base-{envname}.txt",
        'base.in',
    )

    session.run(
        'pip-compile',
        '-o', f"dev-{envname}.txt",
         f"base-{envname}.txt", 'dev.in',
    )


@nox.session(python=['2.7', '3.7'])
def test(session):
    envname = get_envname(session.python)
    session.install('-r', f"requirements/dev-{envname}.txt")

    command = session.posargs or ['pip', 'freeze']
    session.run(*command)
