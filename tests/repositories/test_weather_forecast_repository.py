from src.use_cases.query_weather_forecast.boundaries.weather_forecast_repository_interface import \
    WeatherForecastRepositoryInterface


class WeatherForecastRepository:
    pass


def test_repository_implements_weather_forecast_repository_interface():
    # Arrange
    repository = WeatherForecastRepository()

    # Assert
    assert isinstance(
        repository,
        WeatherForecastRepositoryInterface
    )
