import pytest
from app import app as flask_app


def test_home_status_and_content():
    client = flask_app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Hello, World!' in resp.data
