from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy"
    }


def test_analyze_without_file():
    response = client.post(
        "/analyze",
        data={
            "job_description": (
                "Python developer with SQL"
            )
        }
    )

    assert response.status_code == 422
