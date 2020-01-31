FROM        python:3.6.10-alpine3.10

RUN         mkdir /usr/src/app \
            && apk add --virtual build-deps gcc python-dev musl-dev postgresql-dev

WORKDIR     /usr/src/app

ADD         ./requirements.txt /usr/src/app

RUN         pip install -r requirements.txt

CMD         ["flask", "run", "--host=0.0.0.0"]