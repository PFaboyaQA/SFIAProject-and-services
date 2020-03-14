from application import db
from application.models import Players, Genres, Games

db.drop_all()
db.create_all()
