import pytest
from pytest_bdd import scenario, given, when, then


@pytest.fixture
def context():
    return dict()


@scenario('bdd_test.feature', 'Run a BDD test scenario')
def test_bdd_test():
    pass


@given("a bdd test scenario")
def bdd_test_scenario(context):
    context['name'] = "a bdd test"


@when("I run tests")
def i_run_tests(context):
    context['tested'] = True


@then("this pytest bdd should run")
def verify_bdd_test_ran(context):
    assert 'name' in context
    assert 'tested' in context
    assert context['name'] == "a bdd test"
    assert context['tested']
