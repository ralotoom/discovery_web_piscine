FROM python:3.8-slim

WORKDIR /app

COPY app.py /app/
COPY templates /app/templates/

RUN pip install Flask

EXPOSE 5000


CMD ["python", "app.py"]