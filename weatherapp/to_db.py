import time

from .config import APP_PULL_INTERVAL, APP_TOPONYM
from .consumer import (get_geocode, get_weather_at_location,
                       get_weather_history_at_location)
from .db import weather, weather_insert

if __name__ == "__main__":
    """
    Entry.
    """
    toponym = APP_TOPONYM
    location_data = get_geocode(toponym)
    print('Requested city {}, {} at GPS ({}, {}).'.format(
        location_data.name, location_data.country, location_data.lat, location_data.lon))
    weather_data_list = get_weather_history_at_location(toponym)
    print('Pulling new:', len(weather_data_list))

    inserted = weather_insert(weather_data_list)
    if inserted:
        print('Inserted documents: ', len(inserted))

    try:
        print("Starting to pull in 10 min intervals. Please change the environment \n"
              "variable `APP_PULL_INTERVAL` if you want it more often.")
        while True:
            weather_data = get_weather_at_location(toponym)
            print(str(weather_data).replace(
                '<pyowm.weatherapi25.weather.', '').replace('>', ''))
            weather_insert(weather_data)
            time.sleep(APP_PULL_INTERVAL)
    except KeyboardInterrupt:
        print('Operation canceled.')
    except SystemExit:
        print('System shutting down..')
    finally:
        w_collection = weather()
        print("A total of {} documents in DB.".format(
            w_collection.count_documents({})))
