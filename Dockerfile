FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev && \
    apt-get install -y zip && \
    apt-get install sqlite3

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py
COPY ./database.py /app/database.py
COPY ./loaddata.py /app/loaddata.py
COPY ./templates/index.html /app/templates/index.html

RUN mkdir -p /root/.kaggle
COPY ./kaggle.json /root/.kaggle

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN kaggle datasets download -d docstein/brics-world-bank-indicators
RUN unzip -j brics-world-bank-indicators.zip
RUN python3 database.py
RUN python3 loaddata.py

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
