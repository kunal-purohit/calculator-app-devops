FROM python:3.9-slim

WORKDIR /app

# Copy all the project files into the container at /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]