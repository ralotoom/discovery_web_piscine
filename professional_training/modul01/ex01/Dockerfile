FROM python:2.7

WORKDIR /app
COPY app.py /app/

RUN pip install Flask
RUN pip install lxml
RUN pip install pycrypto

EXPOSE 5000

CMD ["python", "app.py"]
