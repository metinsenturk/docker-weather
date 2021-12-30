FROM python:3.9-slim-buster

WORKDIR /code

COPY Pipfile .
COPY Pipfile.lock .
COPY .env .

# RUN mkdir weatherapp
ADD weatherapp/ weatherapp/

RUN ls -a weatherapp

RUN  pip install pipenv 

# --system --deploy
RUN  PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy

# CMD ["pip", "list"]
# CMD ls -a weatherapp
CMD ["python", "-m", "weatherapp.to_db"]
