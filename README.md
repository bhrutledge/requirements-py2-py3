# Managing requirements in Python 2 and 3 with pip-tools

Comparing [Tox](https://tox.readthedocs.io/) and [Nox](http://nox.thea.codes/), using a subset of requirements from an existing project.

Run the test suite in all environments:

```
$ tox
$ nox
```

Run the test suite in the Python 2.7 environment:

```
$ tox -e py27
$ nox -s test-2.7
```

List outdated dependencies in all environments:

```
$ tox -- pip list -o
$ nox -- pip list -o
```

Recompile requirements in all environments:

```
$ tox -c requirements
$ nox -s requirements
```

Upgrade a primary dependency:

- Add a minimal version specifier to a `requirements/*.in`
    - e.g. `flake8>=3.7` in `requirements/dev.in`
- Recompile

Upgrade a transitive dependency:

- Remove it from all `requirements/*.txt`
- OR add it to a `requirements/*.in`
- Recompile

However, this might not be necessary, because transitive dependencies should be upgraded as needed when a primary dependency is upgraded.
