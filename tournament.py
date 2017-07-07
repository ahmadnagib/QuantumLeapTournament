import bleach
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the matches records from the 'matches' table.
    Sets 'win_count' and 'match_count' columns of 'players' table
    to zero when called
    """
    db_conn = connect()
    cursor = db_conn.cursor()
    query = """ DELETE FROM matches;
                UPDATE players
                SET win_count = DEFAULT, match_count = DEFAULT;
            """
    cursor.execute(query)
    db_conn.commit()
    db_conn.close()
    return


def deletePlayers():
    """Remove all the players records from the 'players' table."""
    db_conn = connect()
    cursor = db_conn.cursor()
    query = "DELETE FROM players;"
    cursor.execute(query)
    db_conn.commit()
    db_conn.close()
    return


def countPlayers():
    """Returns the number of players currently registered
    in 'players' table.
    """
    db_conn = connect()
    cursor = db_conn.cursor()
    query = "SELECT COUNT (id) FROM players;"
    cursor.execute(query)
    result_row = cursor.fetchone()
    db_conn.close()
    return result_row[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.

    Args:
      name: the player's full name.
    """
    # extra unnecessary step to escape any potential
    # passed markup or attributes
    name = bleach.clean(name)
    db_conn = connect()
    cursor = db_conn.cursor()
    # using query parameters to protect from potential SQL injection
    query = "INSERT into players (name) VALUES (%s);"
    cursor.execute(query, (name,))
    db_conn.commit()
    db_conn.close()
    return


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db_conn = connect()
    cursor = db_conn.cursor()
    query = "SELECT * FROM players_standings;"
    cursor.execute(query)
    rows = cursor.fetchall()
    db_conn.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    # extra unnecessary step to escape any potential
    # passed markup or attributes
    winner = bleach.clean(winner)
    loser = bleach.clean(loser)
    db_conn = connect()
    cursor = db_conn.cursor()
    query1 = """
            INSERT into matches (winner, loser) VALUES (%s, %s);
            UPDATE players
            SET win_count = win_count + 1
            WHERE id = %s;
            UPDATE players
            SET match_count = match_count + 1
            WHERE id = %s or id = %s;
            """
    # using query parameters to protect from potential SQL injection
    cursor.execute(query1, ((winner,), (loser,),
                   (winner,), (winner,), (loser,)))
    db_conn.commit()
    db_conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db_conn = connect()
    cursor = db_conn.cursor()
    query = "SELECT id, name FROM players_standings;"
    cursor.execute(query)
    result_list = cursor.fetchall()
    db_conn.close()
    pairs_list = []
    n = 0
    # arranges each two consecutive rows of
    # the result set into one tuple
    for i in range(len(result_list)/2):
        pairs_list.append((result_list[n][0], result_list[n][1],
                          result_list[n+1][0], result_list[n+1][1]))
        n += 2
    return pairs_list
