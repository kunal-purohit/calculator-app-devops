FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir pytest


# Use an official lightweight Python image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the application code into the container
# COPY calculator/ /app/calculator/
# COPY main.py /app/

# # Set the default command to run when the container starts
# CMD ["python", "main.py"]