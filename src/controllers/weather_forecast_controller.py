from src.use_cases.query_weather_forecast.input_dto import InputDTO


class WeatherForecastController:
    def __init__(self, use_case, presenter):
        self.use_case = use_case
        self.presenter = presenter

    def handle(self, request: dict):
        input_dto = InputDTO(
            city=request.get("city")
        )

        return self.use_case.execute(input_dto)
