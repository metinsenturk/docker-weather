# Weather Data App

This app pulls data from [openweathermap.com](https://openweathermap.org/) and adds the data to your mongodb instance. 

Visit:

- http://localhost:8081/ to see the database.

## How to Use It?

1. Register to open weather website and get a key. Free version just fine.
2. Add below environment file, fill your api key there.

    ``` env
    # .env file contents
    MONGODB_HOST=mongodb
    MONGODB_PORT=27017
    MONGODB_USER=root
    MONGODB_PASSWORD=<your-key-here>
    OPEN_WEATHER_API_KEY=<your-key-here>
    ```
3. Run `docker-compose -f "docker-compose.yml" up -d --build` to build and run the containers.
4. That's It!
5. Stop the containers `docker-compose -f 'docker-compose.yml' -p 'docker-weather' stop` after.

## Developing the Python App?

Build the image:

> docker build --pull --rm -f "Dockerfile" -t dockerweather:latest "."

Run a container with local `.env` file.

> docker run --rm -it --env-file .env -p 27017:27017 dockerweather:latest
