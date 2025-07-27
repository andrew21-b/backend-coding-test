from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["status"] == "running"

def test_read_metric_found(monkeypatch):
    def mock_get_metric_result(*args, **kwargs):
        return {"cost_avoided": 123.45}
    monkeypatch.setattr("app.controller.v1.endpoints.metric.get_metric_result", mock_get_metric_result)

    response = client.get("/api/v1/metrics/test_metric_id")
    assert response.status_code == 200
    data = response.json()
    assert "cost_avoided" in data
    assert data["cost_avoided"] == 123.45

def test_read_metric_not_found(monkeypatch):
    def mock_get_metric_result(*args, **kwargs):
        return None
    monkeypatch.setattr("app.controller.v1.endpoints.metric.get_metric_result", mock_get_metric_result)

    response = client.get("/api/v1/metrics/missing_id")
    assert response.status_code == 400
    assert response.json()["detail"] == "Metric not found"