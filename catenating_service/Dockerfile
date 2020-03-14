FROM python:3.5.3

WORKDIR /app

COPY requiremets.txt .

EXPOSE 5000

RUN pip install requests

RUN pip install -r requiremets.txt

ENTRYPOINT '/usr/local/bin/python' 'app.py'

COPY . .

