from random import randint
import string
import random
from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/catenate_player', methods=['GET'])
def catenate_player():
    random_number = requests.get('http://service2:5000/random_number')
    random_string = requests.get('http://service2:5000/random_string')
    app.logger.info(str(random_string.text) + str(random_number.text))
    catenate_player = str(random_string.text) + str(random_number.text)
    return Response(catenate_player, mimetype='text/plain')

@app.route('/catenate_game', methods=['GET'])
def catenate_game():
    random_number = requests.get('http://service3:5000/random_number')
    random_string = requests.get('http://service3:5000/random_string')
    app.logger.info(str(random_string.text) + str(random_number.text))
    catenate_game = str(random_string.text) + str(random_number.text)
    return Response(catenate_game, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

