# Managing dependencies in Python 2 and 3 with pip-tools

Comparing [Tox](https://tox.readthedocs.io/) and [Nox](http://nox.thea.codes/).

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

List outdated requirements in all environments:

```
$ tox -- pip list -o
$ nox -- pip list -o
```

Recompile requirements in all environments:

```
$ tox -c requirements
$ nox -s requirements
```

To upgrade a primary dependency:

- Add a minimal version specifier a `requirements/*.in`
    - e.g. `Django>=2.2` in `requirements/base.in`
- Recompile

To upgrade a transitive dependency:

- Remove it from all `requirements/*.txt`
- OR add it to a `requirements/*.in`
- Recompile
