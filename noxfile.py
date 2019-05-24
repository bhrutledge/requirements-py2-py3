import nox


@nox.session(python=['2.7', '3.7'])
def requirements(session):
    session.install('pip-tools')
    session.run('pip-compile', '-o', f"requirements-{session.python}.txt")


@nox.session(python=['2.7', '3.7'])
def test(session):
    session.install('-r', f"requirements-{session.python}.txt")
    session.run('pip', 'freeze')
