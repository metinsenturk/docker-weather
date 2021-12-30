FROM python:3.9-slim-buster

WORKDIR /code

COPY Pipfile .
COPY Pipfile.lock .
COPY .env .

ADD weatherapp/ weatherapp/

RUN ls -a weatherapp

RUN  pip install pipenv 

RUN  PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy

# CMD ["pip", "list"]
CMD ["python", "-m", "weatherapp.to_db"]
