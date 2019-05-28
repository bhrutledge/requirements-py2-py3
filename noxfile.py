import nox


@nox.session(python=['2.7', '3.7'])
def requirements(session):
    session.install('pip-tools')
    session.chdir('requirements')

    session.run(
        'pip-compile', '-o', f"{session.python}-base.txt",
        'base.in',
    )

    session.run(
        'pip-compile', '-o', f"{session.python}-dev.txt",
         f"{session.python}-base.txt", 'dev.in',
    )


@nox.session(python=['2.7', '3.7'])
def test(session):
    session.install('-r', f"requirements/{session.python}-dev.txt")
    session.run('pip', 'freeze')
