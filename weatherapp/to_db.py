from .consumer import get_weather_at_location, get_weather_history_at_location
from .db import get_weather_collection

if __name__ == "__main__":
    """
    Entry.
    """
    toponym = 'New York, US'
    weather_data_list = get_weather_history_at_location(toponym)

    weather = get_weather_collection()
    weather.find_one()
    weather.insert_many([i.to_dict() for i in weather_data_list])
    total_documents = weather.count_documents({})
    print("A total of {} documents inserted".format(total_documents))
