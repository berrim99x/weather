from unittest.mock import Mock

from src.use_cases.query_weather_forecast.boundaries.presenter_interface import PresenterInterface
from src.use_cases.query_weather_forecast.boundaries.weather_forecast_repository_interface import \
    WeatherForecastRepositoryInterface
from src.use_cases.query_weather_forecast.input_dto import InputDTO
from src.use_cases.query_weather_forecast.use_case import QueryWeatherForecastUseCase


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
