FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ src/
COPY main.py main.py

ENTRYPOINT ["python", "main.py", "--folder_path", "/app/data", "--resolution", "480"]