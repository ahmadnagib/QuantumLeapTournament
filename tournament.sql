-- Table and view definitions for the tournament project

-- checks if there is an existing database with the
-- same name to drop it before creation of a new one
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- connect to the database of interest
\c tournament;

-- create players table
CREATE TABLE players(
   id serial PRIMARY KEY,
   name text NOT NULL
);

-- create matches table
CREATE TABLE matches(
	id serial,
	winner integer REFERENCES players(id),
	loser integer REFERENCES players(id),
	PRIMARY KEY(id, winner, loser)
);


-- create a view getting the count of the matches played by each player
-- by joining players and matches tables
CREATE VIEW players_match_count AS
SELECT players.id AS id, players.name AS name, COUNT(matches.id) AS match_count
FROM players LEFT OUTER JOIN matches
    ON players.id = matches.loser OR players.id = matches.winner
GROUP BY players.id;

-- create a view getting the count of the matches won by each player
-- by joining players and matches tables
CREATE VIEW players_win_count AS
SELECT players.id AS id, COUNT(matches.id) AS win_count
FROM players LEFT OUTER JOIN matches
    ON players.id = matches.winner
GROUP BY players.id;

-- create a players standings view by simply joining the two
-- created views above inspired from udacity reviewer example
CREATE VIEW players_standings AS
SELECT players_match_count.id, players_match_count.name, players_win_count.win_count, players_match_count.match_count
FROM players_win_count JOIN players_match_count
    ON players_match_count.id = players_win_count.id
ORDER BY players_win_count.win_count DESC;
