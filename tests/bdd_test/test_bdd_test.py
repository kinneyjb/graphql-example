import pytest
from functools import partial
from pytest_bdd import parsers, scenario, given, when, then

features_base_dir = './features/'
scenario = partial(scenario, 'bdd_test/bdd_test.feature',
                   features_base_dir=features_base_dir)


@pytest.fixture
def context():
    return dict()


@scenario('Run a BDD test scenario')
def test_bdd_test():
    pass


@scenario('Run a second BDD test scenario')
def test_bdd_test_2():
    pass


@given("a bdd test scenario")
def bdd_test_scenario(context):
    context['name'] = "a bdd test"


@when(parsers.re(r'I run tests.*'))
def i_run_tests(context):
    context['tested'] = True


@then("this pytest bdd should run")
def verify_bdd_test_ran(context):
    assert 'name' in context
    assert 'tested' in context
    assert context['name'] == "a bdd test"
    assert context['tested']
