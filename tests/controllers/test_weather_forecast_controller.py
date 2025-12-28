from unittest.mock import Mock

from src.controllers.weather_forecast_controller import WeatherForecastController
from src.use_cases.query_weather_forecast.use_case import QueryWeatherForecastUseCase
from src.presenters.weather_forecast_presenter import WeatherForecastPresenter


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
