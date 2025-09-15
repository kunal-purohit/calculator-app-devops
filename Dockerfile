FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY calculator/ ./calculator
# COPY tests/ ./tests

CMD ["python", "main.py"]
