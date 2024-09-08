import json

import requests
from dateutil import parser

from src.constants import DAYS_TUPLE


class WeatherParser:
    @staticmethod
    def get_weather() -> dict[str, float]:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast?latitude=55.7522&longitude=37.6156&hourly=temperature_2m"
            "&past_days=6&forecast_days=1"
        )
        data = json.loads(response.text)
        dates = data["hourly"]["time"]
        temperatures = data["hourly"]["temperature_2m"]

        weather = dict()
        for time, temperature in zip(dates, temperatures):
            dt = parser.parse(time)
            day_name = DAYS_TUPLE[dt.weekday()]
            if day_name in weather:
                weather[day_name].append(temperature)
            else:
                weather[day_name] = [temperature]

        for day in weather.keys():
            weather[day] = round(sum(weather[day]) / len(weather[day]), 2)

        return weather
