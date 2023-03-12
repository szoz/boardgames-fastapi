import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture(scope="session")
def client() -> TestClient:
    """Return FastAPI test client."""
    return TestClient(app)
