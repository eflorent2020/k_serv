from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/test.db' # TODO mettre env variable & update makefile
db = SQLAlchemy(app)

from api.controller import index
from api.controller import batchs
from api.controller import signboards