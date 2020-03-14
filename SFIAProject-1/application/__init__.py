from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DB_URI'))
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from application import routes

