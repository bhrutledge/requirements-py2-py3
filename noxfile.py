import nox


@nox.session(python=['2.7', '3.7'])
def requirements(session):
    session.install('pip-tools')

    session.run(
        'pip-compile', '-o', f"requirements-{session.python}.txt",
        'requirements.in',
    )

    session.run(
        'pip-compile', '-o', f"requirements-{session.python}-dev.txt",
         f"requirements-{session.python}.txt",
         'requirements-dev.in',
    )


@nox.session(python=['2.7', '3.7'])
def test(session):
    session.install('-r', f"requirements-{session.python}-dev.txt")
    session.run('pip', 'freeze')
