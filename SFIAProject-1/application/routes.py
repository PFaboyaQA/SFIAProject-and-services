from flask import render_template, url_for, redirect, Response
from application import app, db
from application.forms import AddGenreForm, AddGameForm, PlayerForm, DeleteForm, UpdateForm, DeleteGenreForm, DeleteGameForm, AddPlayerGame
from application.models import Players, Genres, Games
import requests

@app.route('/')
@app.route('/home')
def home():
        playerData = Players.query.all()
        return render_template('home.html', title='Home', players=playerData)

@app.route('/genre', methods=['GET', 'POST'])
def genre():
        add_genre = AddGenreForm()
        if add_genre.validate_on_submit():
                add_genre_to_db = Genres(
				genre_name = add_genre.genre_name.data,
				)
                db.session.add(add_genre_to_db)
                db.session.commit()
                return redirect(url_for('genre'))
        else:
	        print(add_genre.errors)
	        genreData = Genres.query.all()
        return render_template('genre.html', title='Genres', genres=genreData, form=add_genre)

@app.route('/game', methods=['GET', 'POST'])
def game():
        add_game = AddGameForm()
        if add_game.validate_on_submit():
                game_reg_id = requests.get('http://service4:5000/catenate_game')
                add_game_to_db = Games(
                                game_name = add_game.game_name.data,
                                Price = add_game.price.data,
                                company = add_game.company.data,
                                main_platform = add_game.main_platform.data,
                                buyer_id = add_game.buyer_id.data,
                                genre_id = add_game.genre_id.data,
                                game_registration_id = game_reg_id.text
                                )
                db.session.add(add_game_to_db)
                db.session.commit()
                app.logger.info(game_reg_id.text)
                return redirect(url_for('game'))
        else:
                print(add_game.errors)
                gameData = Games.query.all()
        return render_template('game.html', title='Game', games=gameData, form=add_game)

@app.route('/register', methods=['GET', 'POST'])
def post():
        form = PlayerForm()
        app.logger.info('check')
        if form.validate_on_submit():
                player_reg_id = requests.get('http://service4:5000/catenate_player')
                playerData = Players(
                        first_name = form.first_name.data,
                        last_name = form.last_name.data,
                        email = form.email.data,
                        player_registration_id = player_reg_id.text
                        )
                db.session.add(playerData)
                db.session.commit()
                app.logger.info(player_reg_id.text)
                return redirect(url_for('home'))
        else:
                print(form.errors)

        return render_template('post.html', title='post', form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete(): 
            delete = DeleteForm()
            if delete.validate_on_submit():
                customer = Players.query.filter_by(first_name=delete.player_firstname.data, last_name=delete.player_lastname.data).first()
                db.session.delete(customer)
                db.session.commit()
                return redirect (url_for('home'))
            delete_genre = DeleteGenreForm()
            if delete_genre.validate_on_submit():
                category = Genres.query.filter_by(genre_name=delete_genre.genrename.data).first()
                db.session.delete(category)
                db.session.commit()
                return redirect (url_for('genre'))
            delete_game = DeleteGameForm()
            if delete_game.validate_on_submit():
                item = Games.query.filter_by(game_name=delete_game.gamename.data).first()
                db.session.delete(item)
                db.session.commit()
                return redirect (url_for('game'))
            return render_template('delete.html', title='Delete', delete=delete, delete_genre=delete_genre, delete_game=delete_game)
            
@app.route('/home/<player_id>', methods=['GET','POST'])
def playerid(player_id):
    playerData = Players.query.filter_by(player_id=player_id).first()
    print(playerData)
    form = UpdateForm()
    if form.validate_on_submit():
        playerData.first_name=form.first_name.data
        playerData.last_name=form.last_name.data
        playerData.email=form.email.data
        db.session.add(playerData)
        db.session.commit()
        return redirect (url_for('home'))
    return render_template('playerid.html', title='Player', player=playerData, form=form)

@app.route('/genre/<genre_id>', methods=['GET'])
def genreid(genre_id):
    genreData = Genres.query.filter_by(genre_id=genre_id).first()
    return render_template('genreid.html', title='Genre', genre=genreData)
