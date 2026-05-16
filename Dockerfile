FROM python:3.12

WORKDIR /app

COPY requirments.txt .
RUN pip install -r requirments.txt

COPY weather.py .

CMD ["python", "weather.py"]