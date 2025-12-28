from src.repositories.in_memory_weather_forecast_repository import (
    InMemoryWeatherForecastRepository,
)


def test_in_memory_repository_returns_data_when_city_exists():
    repo = InMemoryWeatherForecastRepository(
        data={
            "Algiers": {"temp": 22}
        }
    )

    result = repo.get("Algiers")

    assert result == {"temp": 22}


def test_in_memory_repository_returns_none_when_city_not_exists():
    repo = InMemoryWeatherForecastRepository(data={})

    result = repo.get("Unknown")

    assert result is None
