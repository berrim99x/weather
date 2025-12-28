from src.use_cases.query_weather_forecast.output_dto import OutputDTO
from src.use_cases.query_weather_forecast.boundaries.weather_forecast_repository_interface import (
    WeatherForecastRepositoryInterface,
)
from src.use_cases.query_weather_forecast.boundaries.presenter_interface import (
    PresenterInterface,
)


class QueryWeatherForecastUseCase:
    def __init__(
        self,
        weather_forecast_repository: WeatherForecastRepositoryInterface,
        presenter: PresenterInterface,
    ):
        self.weather_forecast_repository = weather_forecast_repository
        self.presenter = presenter

    def execute(self, input_dto):
        forecast = self.weather_forecast_repository.get(input_dto.city)

        output = self._build_output(forecast)
        return self.presenter.present(output)

    def _build_output(self, forecast):
        if forecast is None:
            return OutputDTO(
                success=False,
                weather_data=None,
            )

        return OutputDTO(
            success=True,
            weather_data=forecast,
        )
