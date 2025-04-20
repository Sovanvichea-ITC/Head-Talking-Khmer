# Use Python 3.8 base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y build-essential python3.8-dev libsndfile1

# Copy the requirements.txt file and install Python packages
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . /app/
