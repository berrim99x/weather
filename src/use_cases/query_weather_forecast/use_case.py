from src.use_cases.query_weather_forecast.output_dto import OutputDTO


class QueryWeatherForecastUseCase:
    def __init__(self, weather_forecast_repository, presenter):
        self.weather_forecast_repository = weather_forecast_repository
        self.presenter = presenter

    def execute(self, input_dto):
        forecast = self.weather_forecast_repository.get(input_dto.city)

        if forecast is None:
            self.presenter.present(
                OutputDTO(success=False, weather_data=None)
            )
        else:
            self.presenter.present(
                OutputDTO(success=True, weather_data=forecast)
            )
