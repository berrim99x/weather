from fastapi import FastAPI

from src.controllers.weather_forecast_controller import WeatherForecastController
from src.presenters.weather_forecast_presenter import WeatherForecastPresenter
from src.use_cases.query_weather_forecast.use_case import QueryWeatherForecastUseCase
from src.repositories.in_memory_weather_forecast_repository import (
    InMemoryWeatherForecastRepository,
)

app = FastAPI()


@app.get("/weather")
def get_weather(city: str):
    # Fake repository (no data)
    repository = InMemoryWeatherForecastRepository(data={})

    presenter = WeatherForecastPresenter()
    use_case = QueryWeatherForecastUseCase(
        weather_forecast_repository=repository,
        presenter=presenter,
    )
    controller = WeatherForecastController(
        use_case=use_case,
        presenter=presenter,
    )

    return controller.handle(
        {"city": city}
    )
