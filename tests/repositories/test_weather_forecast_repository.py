from src.repositories.weather_forecast_repository import WeatherForecastRepository
from src.use_cases.query_weather_forecast.boundaries.weather_forecast_repository_interface import (
    WeatherForecastRepositoryInterface,
)


def test_repository_implements_weather_forecast_repository_interface():
    repository = WeatherForecastRepository()

    assert isinstance(
        repository,
        WeatherForecastRepositoryInterface
    )
