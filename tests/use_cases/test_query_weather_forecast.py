from unittest.mock import Mock



class InputDTO:
    def __init__(self, city: str):
        self.city = city

class OutputDTO:
    def __init__(self, success: bool, weather_data=None):
        self.success = success
        self.weather_data = weather_data


class PresenterInterface:
    def present(self, output_dto):
        raise NotImplementedError


class WeatherForecastRepositoryInterface:
    def get(self, city: str):
        raise NotImplementedError
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


def test_should_present_unsuccess_when_weather_forecast_does_not_exist():
    # Arrange
    weather_forecast_repository = Mock(spec=WeatherForecastRepositoryInterface)
    weather_forecast_repository.get.return_value = None

    presenter = Mock(spec=PresenterInterface)

    use_case = QueryWeatherForecastUseCase(
        weather_forecast_repository,
        presenter,
    )

    input_dto = InputDTO(city="Algiers")

    # Act
    use_case.execute(input_dto)

    # Assert
    presenter.present.assert_called_once()
    output_dto = presenter.present.call_args.args[0]

    assert output_dto.success is False
