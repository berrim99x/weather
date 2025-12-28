from typing import Dict, Any, Optional
from src.use_cases.query_weather_forecast.boundaries.weather_forecast_repository_interface import (
    WeatherForecastRepositoryInterface,
)


class InMemoryWeatherForecastRepository(WeatherForecastRepositoryInterface):
    def __init__(self, data: Dict[str, Dict[str, Any]]):
        self._data = data

    def get(self, city: str) -> Optional[Dict[str, Any]]:
        return self._data.get(city)
