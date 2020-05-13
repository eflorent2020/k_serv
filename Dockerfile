from python:3

WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 init_db.py && FLASK_APP=server.py flask run --host=0.0.0.0
