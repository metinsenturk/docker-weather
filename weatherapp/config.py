import os

# mongo db settings
MONGODB_HOST = os.environ.get('MONGODB_HOST')
MONGODB_PORT = os.environ.get('MONGODB_PORT')
MONGODB_USER = os.environ.get('MONGODB_USER')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')

# open weather app key
OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')

# local app settings
APP_TOPONYM = os.environ.get('APP_TOPONYM', 'Istanbul, TR')
APP_PULL_INTERVAL = os.environ.get('APP_PULL_INTERVAL', 60 * 10)
