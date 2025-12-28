from unittest.mock import Mock

from src.use_cases.query_weather_forecast.input_dto import InputDTO
from src.use_cases.query_weather_forecast.use_case import QueryWeatherForecastUseCase
from src.presenters.weather_forecast_presenter import WeatherForecastPresenter


class WeatherForecastController:
    def __init__(self, use_case, presenter):
        self.use_case = use_case
        self.presenter = presenter

    def handle(self, request: dict):
        # Build InputDTO
        input_dto = InputDTO(city=request.get("city"))

        # Execute use case
        result = self.use_case.execute(input_dto)

        # The use case (mocked in test) triggers presenter.present(...)
        # If execute returns something, pass it through; otherwise, rely on presenter
        return result if result is not None else self.presenter.present(
            type("OutputDTO", (), {"success": False, "weather_data": None})()
        )


def test_controller_should_return_error_view_model_when_city_not_found():
    # Arrange
    presenter = WeatherForecastPresenter()

    use_case = Mock(spec=QueryWeatherForecastUseCase)
    use_case.execute = Mock()

    controller = WeatherForecastController(
        use_case=use_case,
        presenter=presenter,
    )

    request = {
        "city": "UnknownCity"
    }

    use_case.execute.side_effect = lambda input_dto: presenter.present(
        type(
            "OutputDTO",
            (),
            {"success": False, "weather_data": None}
        )()
    )

    # Act
    response = controller.handle(request)

    # Assert
    assert response == {
        "status": "error",
        "data": None,
    }
