Feature: test pytest bdd is setup correctly
    Scenario: Run a BDD test scenario
        Given a bdd test scenario
        When I run tests
        Then this pytest bdd should run
    Scenario: Run a second BDD test scenario
        Given a bdd test scenario
        When I run tests again
        Then this pytest bdd should run
