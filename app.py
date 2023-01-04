from flask import Flask, jsonify, request
from score_database.Snake_DB_utils import get_leaderboard, get_high_score, get_game_history
from score_database.Snake_DB_utils import add_new_player, log_score, check_if_new_player

app = Flask(__name__)

# line of code below means that dicts will retain order when sent to url (default is alphabetical sorting)
# so order from DB queries is preserved in API
app.config["JSON_SORT_KEYS"] = False


# Welcome to our API!
@app.route('/', methods=['GET'])
def welcome():
    # converting string to correct format for API (converted to JSON and a flask Response object)
    message = jsonify('Welcome to the Snake Data Service')
    return message

# http://127.0.0.1:5001

# GETTING INFO FROM DB

# checking if player exists in DB
@app.route('/<name>', methods=['GET'])      # GET is default method so don't actually need to specify this param
def get_name(name):
    name = check_if_new_player(name)
    return jsonify(name)

# http://127.0.0.1:5001/**name argument here**

# requesting leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaders():
    leaders = get_leaderboard()
    return jsonify(leaders)

# http://127.0.0.1:5001/leaderboard


# requesting player's top score
@app.route('/top_score/<name>', methods=['GET'])
def get_top_score(name):
    top_score = get_high_score(name)
    return jsonify(top_score)

# http://127.0.0.1:5001/top_score/**name argument here**


# requesting game history for a player
@app.route('/history/<name>', methods=['GET'])
def get_history(name):
    history = get_game_history(name)
    return jsonify(history)

# http://127.0.0.1:5001/history/**name argument here**


# ADDING INFO TO DB

# adding a new player to DB
@app.route('/post_player', methods=['POST'])
def post_player():
    player = request.get_json()
    add_new_player(player['name'])
    message = 'Welcome, {}! You have been added to the CFG Snake Database.'.format(player['name'])
    return jsonify(message)


# adding a new score log to DB
@app.route('/post_score', methods=['POST'])
def post_score():
    new_score = request.get_json()
    log_score(new_score['name'], new_score['date_time'], new_score['score'])
    message = ('Your score has been saved in the CFG Snake Database. Woop!')
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
