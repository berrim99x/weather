from fastapi.testclient import TestClient
from src.main import app



def test_get_weather_returns_error_when_city_not_found():
    client = TestClient(app)

    response = client.get(
        "/weather",
        params={"city": "UnknownCity"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": "error",
        "data": None,
    }
