from typing import List

from pyowm.owm import OWM
from pyowm.weatherapi25.observation import Observation
from pyowm.weatherapi25.one_call import OneCall
from pyowm.weatherapi25.weather import Weather

from .config import OPEN_WEATHER_API_KEY

owm = OWM(OPEN_WEATHER_API_KEY)


def get_weather_at_location(toponym: str) -> Weather:
    """
    Weather information at a location. New info every 10 min.
    """
    wm = owm.weather_manager()
    onservation: Observation = wm.weather_at_place(toponym)
    return onservation.weather


def get_weather_history_at_location(toponym: str) -> List[Weather]:
    """
    Historical weather information at a location. Free API pulls
    5 days only.
    """
    wm = owm.weather_manager()
    gm = owm.geocoding_manager()

    locations = gm.geocode(toponym)
    for location in locations:
        location.to_dict()

    onecall: OneCall = wm.one_call_history(location.lat, location.lon)

    forecasts = []
    forecasts.append(onecall.current)
    if onecall.forecast_minutely is not None:
        forecasts.extend(onecall.forecast_minutely)
    if onecall.forecast_hourly is not None:
        forecasts.extend(onecall.forecast_hourly)
    if onecall.forecast_daily is not None:
        forecasts.extend(onecall.forecast_daily)
    return forecasts
