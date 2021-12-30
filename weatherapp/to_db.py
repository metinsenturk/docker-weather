import time

from .consumer import get_weather_at_location, get_weather_history_at_location
from .db import weather, weather_insert

if __name__ == "__main__":
    """
    Entry.
    """
    toponym = 'New York, US'
    weather_data_list = get_weather_history_at_location(toponym)
    print('Pulling new:', len(weather_data_list))

    inserted = weather_insert(weather_data_list)
    if inserted:
        print('Inserted documents: ', len(inserted))

    try:
        while True:
            weather_data = get_weather_at_location(toponym)
            print(str(weather_data).replace(
                '<pyowm.weatherapi25.weather.', '').replace('>', ''))
            weather_insert(weather_data)
            time.sleep(5)
    except KeyboardInterrupt:
        print('Operation canceled.')
    except SystemExit:
        print('System shutting down..')
    finally:
        w_collection = weather()
        print("A total of {} documents in DB.".format(
            w_collection.count_documents({})))
