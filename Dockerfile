FROM ubuntu
RUN apt-get update -y && \
    apt-get install -y python3-pip

ENV FLASKMODE=server

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./app /app

EXPOSE 80

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
