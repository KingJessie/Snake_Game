import mysql.connector
from config import USER, PASSWORD, HOST


# custom error to raise when there is problem with the python-DB connection
class DbConnectionError(Exception):
    pass


# establishing a session with the MySQL server
def _connect_to_db():
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database='snake'
    )
    return connection


# checking if player already in DB
def check_if_new_player(name):
    try:
        db_connection = _connect_to_db()
        my_cursor = db_connection.cursor()
        print("Connected to snake DB")

        query = "SELECT name FROM player_name WHERE name = '{}'".format(name)

        my_cursor.execute(query)
        result = my_cursor.fetchall()
        # checking if a name exists in the returned list
        if len(result) == 1:
            player_exists = True
        elif len(result) == 0:
            player_exists = False

        my_cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB!")

    finally:
        if db_connection:
            db_connection.close()
            print("Connection to snake DB is closed")

    print("I checked the DB")
    return player_exists



# inserting new player into DB
def add_new_player(name):
    try:
        db_connection = _connect_to_db()
        my_cursor = db_connection.cursor()
        print("Connected to snake DB")

        query = "INSERT INTO player_name (name) VALUES ('{}')".format(name)

        my_cursor.execute(query)
        db_connection.commit()
        my_cursor.close()

    except Exception:
        raise DbConnectionError("Failed to add new player to database!")

    finally:
        if db_connection:
            db_connection.close()
            print("Connection to snake DB is closed")

    print("New player added to DB")


# inserting a new record (player name, datetime, and score) into the score log table
# will only work if the name already exists in player_name table (primary key)
def log_score(name, date_time, score):
    try:
        db_connection = _connect_to_db()
        my_cursor = db_connection.cursor()
        print("Connected to snake DB")

        query = "INSERT INTO score_log (name, date_time, score) VALUES ('{}', '{}', {})".format(name, date_time, score)

        my_cursor.execute(query)
        db_connection.commit()
        my_cursor.close()

    except Exception:
        raise DbConnectionError("Failed to log game in database!")

    finally:
        if db_connection:
            db_connection.close()
            print("Connection to snake DB is closed")

    print("Game logged in DB")


# get the top 10 scorers from the leaderboard view (which automatically updates every time the score_log table is updated)
def get_leaderboard():
    try:
        db_connection = _connect_to_db()
        my_cursor = db_connection.cursor()
        print("Connected to snake DB")

        query ="SELECT * FROM leaderboard ORDER BY high_score DESC"

        my_cursor.execute(query)

        result = my_cursor.fetchall()  # fetchall() returns all rows as a list of tuples
        leaders = dict(result) # order of leaders will be preserved (dicts are ordered, since Python 3.7)
        my_cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return leaders


# get the highest score for a single player
def get_high_score(name):
    try:
        db_connection = _connect_to_db()
        my_cursor = db_connection.cursor()
        print("Connected to snake DB")

        query ="SELECT name, MAX(score) as high_score FROM score_log WHERE name = '{}'".format(name)

        my_cursor.execute(query)

        result = my_cursor.fetchall()
        high_score = dict(result)   # converting the list of (one) tuple to a dict

        my_cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return high_score

# mapping player's name and game history to a nested dictionary format (for get_game_history function below)
def map_game_history(result):
    list_of_dicts = []
    for i in result:
        dict = {'date_time': i[0], 'score': i[1]}
        list_of_dicts.append(dict)
    return list_of_dicts


# get all score logs for a single player
def get_game_history(name):
    try:
        db_connection = _connect_to_db()
        my_cursor = db_connection.cursor()
        print("Connected to snake DB")

        query ="SELECT date_time, score FROM score_log WHERE name = '{}' ORDER BY date_time DESC;".format(name)

        my_cursor.execute(query)

        result = my_cursor.fetchall()
        history = {'Player name': name, 'Score log': map_game_history(result)}

        my_cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return history



if __name__ == '__main__':
    pass




