FROM python:3.9-slim-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # mariadb dependencies
  && apt-get install -y default-libmysqlclient-dev \
  # Additional dependencies
  && apt-get install -y telnet netcat libcairo2-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
  
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]
