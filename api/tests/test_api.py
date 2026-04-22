from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app

client = TestClient(app)


# -------------------------
# MOCK REDIS SETUP
# -------------------------
@patch("main.redis")
def test_create_job(mock_redis):
    mock_redis.rpush = MagicMock(return_value=1)

    response = client.post("/jobs")

    assert response.status_code == 200
    assert "job_id" in response.json()


@patch("main.redis")
def test_health(mock_redis):
    mock_redis.ping = MagicMock(return_value=True)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@patch("main.redis")
def test_get_job_invalid(mock_redis):
    mock_redis.get.return_value = None

    response = client.get("/jobs/invalid-id")

    assert response.status_code == 200
    assert "error" in response.json()