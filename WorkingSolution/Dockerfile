# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /WebApp

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run run.py when the container launches
CMD ["python", "run.py"]
