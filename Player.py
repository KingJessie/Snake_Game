import requests
from datetime import datetime


class Player:
    """ Represents single player of CFG Snake game."""

    # To initialise Player object:
    # get player name from user input
    # check if player is in DB...
    # ...if not, add player to DB
    def __init__(self):
        self.name = input('Enter your player name: ')
        self.player_status = self.get_player_status()
        self.database_action = self.add_player_to_DB()


# check if player is new, or already exists in DB, using API
    def get_player_status(self):
        # see if player is in DB with GET request
        result = requests.get('http://127.0.0.1:5001/{}'.format(self.name))
        boolean = result.json()
        return boolean

# add player to DB using API
    def add_player_to_DB(self):
        if self.get_player_status() == False:
            # add player to API with POST request
            player = {'name': self.name}
            result = requests.post('http://127.0.0.1:5001/post_player', json=player)
            message_from_server = result.json()
            print(message_from_server)
        elif self.get_player_status() == True:
            print("Welcome back, {}!".format(self.name))

# log a game in the DB using API
    def log_score(self, snake_length):
        date_time = datetime.now().strftime("%Y-%m-%d_%H:%M")
        score = snake_length - 3
        log_data = {'name': self.name, 'date_time': date_time, 'score': score}
        result = requests.post('http://127.0.0.1:5001/post_score', json=log_data)
        message_from_server = result.json()
        print(message_from_server)


if __name__ == '__main__':
    pass






