from typing import Optional, Dict, Any
from src.use_cases.query_weather_forecast.boundaries.weather_forecast_repository_interface import (
    WeatherForecastRepositoryInterface,
)


class WeatherForecastRepository(WeatherForecastRepositoryInterface):
    def get(self, city: str) -> Optional[Dict[str, Any]]:
        return None
