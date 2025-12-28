from abc import ABC, abstractmethod

class WeatherForecastRepositoryInterface(ABC):
    @abstractmethod
    def get(self, city: str):
        raise NotImplementedError

class WeatherForecastRepository(WeatherForecastRepositoryInterface):
    def get(self, city: str):
        return None

def test_repository_implements_weather_forecast_repository_interface():
    # Arrange
    repository = WeatherForecastRepository()

    # Assert
    assert isinstance(
        repository,
        WeatherForecastRepositoryInterface
    )
