import pytest
from app import create_app


@pytest.fixture
def test_config():
    config = dict(HELLO_MESSAGE='Hello, Testing!')
    return config


@pytest.fixture
def app(test_config):
    app = create_app(test_config=test_config)
    return app
