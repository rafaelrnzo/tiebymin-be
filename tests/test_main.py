
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "docs_url" in data
    assert "health_check" in data


def test_health_endpoint():
    """Test health check endpoint."""
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "message" in data
    assert data["status"] in ["healthy", "unhealthy"]
