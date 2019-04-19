FROM python:3.6-alpine

RUN adduser -D project

WORKDIR /home/project

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY start.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP start.py

RUN chown -R project:project ./
USER project

EXPOSE 5001
ENTRYPOINT ["./boot.sh"]
