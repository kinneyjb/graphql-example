# Example 

* A quick experiment based on [https://graphene-python.org/](https://graphene-python.org/).
* This is based on [graphene-python/graphene-sqlachemy](https://github.com/graphql-python/graphene-sqlalchemy/tree/master/examples/flask_sqlalchemy).

## Packages used
Check out the [Pipefile](src/Pipfile)

```yaml
[packages]
graphene = "*"
sqlalchemy = "*"
graphene-sqlalchemy = "*"
flask = "*"
flask-graphql = "*"

[dev-packages]
"flake8" = "*"
pytest = "*"
behave = "*"
pytest-bdd = "*"
pytest-flask = "*"
```

## development with pipenv


Use [pipenv](https://pipenv.readthedocs.io/en/latest/) to set up the python virtual environmet.
```bash
$ pipenv sync --dev
```

Use `pipenv run` to run the [pytest](https://docs.pytest.org/en/latest/) tests.

```bash
$ pipenv run pytest
```

Use `pipenv` in [development](https://pipenv.readthedocs.io/en/latest/advanced/#community-integrations).

```bash
$ pipenv shell
$ vim # etc...
```

### testing

Something mildly curious... bdd tests using `pytest-bdd`.
TODO: implement actual bdd tests.

* [bdd_test.feature](src/tests/features/bdd_test/bdd_test.feature)
* [test_bdd_test.py](src/tests/bdd_test/test_bdd_test.py)

And pytests to test the graphql.

* [conftest.py](src/tests/flask/conftest.py)
* [test_graphql_query.py](src/tests/flask/test_graphql_query.py)

The tests and flask service are hardcoded to use the sqlite db `src/database.sqlite3`.
The sqlite db was generated using [generate_database.py](src/generate_database.py).

### running

Use `pipenv` to run the flask app.

```bash
$ pipenv run flask run
```

Goto [http://localhost:5000/graphql](http://localhost:5000/graphql).

![GraphiQL](graphiql-ui.png)
