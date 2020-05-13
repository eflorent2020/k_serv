from flask import Flask
from waitress import serve

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# os.path.join
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/test.db' # TODO mettre env variable & update makefile
db = SQLAlchemy(app)

from api.controller import index
from api.controller import batchs
from api.controller import signboards

if __name__ == "__main__":
   serve(app, host='0.0.0.0', port=8000)

