# Use official Python base image
FROM python:alpine

# Set working directory
WORKDIR /myapp

# Copy your Python script into the container
COPY sql_demo.py .

# Install MySQL connector
RUN pip install mysql-connector-python

# Default command to run your app
CMD ["python", "sql_demo.py"]
