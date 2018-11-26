from flask import url_for


def test_hello(client):
    result = client.get(url_for('hello'))
    assert result.status_code == 200
    assert "Hello, Testing!" == result.data.decode("utf-8")
