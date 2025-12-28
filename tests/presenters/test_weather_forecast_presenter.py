from src.use_cases.query_weather_forecast.output_dto import OutputDTO


class WeatherForecastPresenter:
    pass


def test_presenter_should_return_error_view_model_when_unsuccessful():
    # Arrange
    presenter = WeatherForecastPresenter()
    output_dto = OutputDTO(
        success=False,
        weather_data=None,
    )

    # Act
    view_model = presenter.present(output_dto)

    # Assert
    assert view_model == {
        "status": "error",
        "data": None,
    }
