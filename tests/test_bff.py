from fastapi.testclient import TestClient # type: ignore
from app.main import app

client = TestClient(app)

def test_bff():
    response = client.get("/bff/user/1", headers={"x-api-key": "default-secret-key"})
    assert response.status_code == 200
    assert "user" in response.json()
    assert "recommended_products" in response.json()
