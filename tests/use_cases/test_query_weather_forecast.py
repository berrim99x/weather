from unittest.mock import Mock



class InputDTO:
    pass
class OutputDTO:
    pass

class PresenterInterface:
    pass

class WeatherForecastRepositoryInterface:
    pass

class QueryWeatherForecastUseCase:
    pass

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
