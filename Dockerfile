FROM python:2.7.10

RUN apt-get update; apt-get install -y postgresql-client-9.4 cowsay

ENV PATH $PATH:/usr/games

ADD ./server.py /etc/server.py

CMD /etc/server.py