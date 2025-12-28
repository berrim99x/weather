class WeatherForecastPresenter:
    def present(self, output_dto):
        return {
            "status": "success" if output_dto.success else "error",
            "data": output_dto.weather_data,
        }
