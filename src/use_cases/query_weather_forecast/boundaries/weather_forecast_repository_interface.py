from abc import ABC, abstractmethod
from typing import Optional, Dict, Any


class WeatherForecastRepositoryInterface(ABC):
    @abstractmethod
    def get(self, city: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError
