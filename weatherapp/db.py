from urllib.parse import quote_plus

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from .config import MONGODB_HOST, MONGODB_PASSWORD, MONGODB_PORT, MONGODB_USER

CONNECTION_STRING = "mongodb://%s:%s@%s:%s" % (
    quote_plus(MONGODB_USER), quote_plus(MONGODB_PASSWORD), MONGODB_HOST, MONGODB_PORT)


def get_database() -> Database:

    client = MongoClient(CONNECTION_STRING)
    return client['WeatherDB']


def get_weather_collection() -> Collection:

    db = get_database()
    return db['WeatherCollection']
