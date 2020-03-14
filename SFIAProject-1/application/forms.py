from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, Email
from application.models import Players, Genres, Games
from application import app


class PlayerForm(FlaskForm):
        first_name = StringField('First Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        last_name = StringField('Last Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        email = StringField('Email',
                validators = [
                        DataRequired(),
                        Email()
                ]
        )
        submit = SubmitField('Post!')

class AddGenreForm(FlaskForm):
        genre_name = StringField('Genre Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        submit = SubmitField('Add!')

class AddGameForm(FlaskForm):
        game_name = StringField('Game Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        price = DecimalField('Price', places=2,
                validators = [
                        DataRequired()
                ]
        )
        company = StringField('Company',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        main_platform = StringField('main platform',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        buyer_id = IntegerField('Buyer ID',
                validators = [
                        NumberRange(min=1, max=100)
                ]
        )
        genre_id = IntegerField('Genre ID',
                validators = [
                        DataRequired(),
                        NumberRange(min=1, max=100)
                ]
        )
        submit = SubmitField('Add!')

class UpdateForm(FlaskForm):
        first_name = StringField('First Name',
                validators = [  
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        last_name = StringField('Last Name',
                        validators = [
                                DataRequired(),
                                Length(min=2, max=30)
                        ]
        )
        email = StringField('email',
                        validators = [
                                DataRequired(),
                                Email()
                        ]
        )
        submit = SubmitField('Update')

class DeleteForm(FlaskForm):
        player_firstname = StringField('First Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        player_lastname = StringField('Last Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        submit = SubmitField('Delete Player')

class DeleteGenreForm(FlaskForm):
        genrename = StringField('Genre Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                    ]
        )
        submit = SubmitField('Delete Genre')

class DeleteGameForm(FlaskForm):
        gamename = StringField('Game Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        submit = SubmitField('Delete Game')

class AddPlayerGame(FlaskForm):
        game_name = StringField('Game Name',
                validators = [
                        DataRequired(),
                        Length(min=2, max=30)
                    ]
        )
        submit = SubmitField('Change!')
