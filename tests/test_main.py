import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    """Return FastAPI test client"""
    return TestClient(app)


def test_read_main(client):
    """Test root endpoint response status code and payload."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
