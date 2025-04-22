FROM python:alpine

WORKDIR /myapp

COPY sql_demo.py .

RUN pip install mysql-connector-python

CMD ["python", "sql_demo.py"]
