FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir pytest

# Copy the application code into the container
COPY calculator/ /app/calculator/
COPY main.py /app/

# Set the default command to run when the container starts
CMD ["python", "main.py"]