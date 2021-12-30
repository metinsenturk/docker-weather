from typing import Any, List, Union
from urllib.parse import quote_plus

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pyowm.weatherapi25.weather import Weather

from .config import MONGODB_HOST, MONGODB_PASSWORD, MONGODB_PORT, MONGODB_USER

CONNECTION_STRING = "mongodb://%s:%s@%s:%s" % (
    quote_plus(MONGODB_USER), quote_plus(MONGODB_PASSWORD), MONGODB_HOST, MONGODB_PORT)


def get_database() -> Database:

    client = MongoClient(CONNECTION_STRING)
    return client['WeatherDB']


def weather() -> Collection:

    db = get_database()
    return db['WeatherCollection']


def weather_get_all() -> List[Any]:

    return list(weather().find())


def weather_insert(document: Union[Weather, List[Weather]]) -> List[Any]:
    """
    Insert any weather data to collection.
    """
    w_colection = weather()
    results = []

    if isinstance(document, Weather):
        from_db = w_colection.find_one(
            {'reference_time': document.reference_time()})
        if from_db is None:
            result = w_colection.insert_one(document.to_dict()).inserted_id
            results.append(result)

    else:
        documents = document
        reference_times = [w.reference_time() for w in documents]
        cursor = w_colection.find(
            {
                'reference_time': {
                    '$in': reference_times
                }
            },
            ['reference_time']
        )
        reference_times_exists = [i.get('reference_time') for i in cursor]

        to_insert_list = [
            i.to_dict()
            for i in documents
            if i.reference_time() not in reference_times_exists
        ]
        results = w_colection.insert_many(to_insert_list).inserted_ids

    return results
