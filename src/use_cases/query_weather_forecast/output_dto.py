class OutputDTO:
    def __init__(self, success: bool, weather_data=None):
        self.success = success
        self.weather_data = weather_data
