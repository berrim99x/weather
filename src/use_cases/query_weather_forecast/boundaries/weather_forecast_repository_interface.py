class WeatherForecastRepositoryInterface:
    def get(self, city: str):
        raise NotImplementedError
