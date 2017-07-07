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
   name text NOT NULL,
   win_count integer NOT NULL DEFAULT 0,
   match_count integer NOT NULL DEFAULT 0
);

-- create matches table
CREATE TABLE matches(
	id serial,
	winner integer REFERENCES players(id),
	loser integer REFERENCES players(id),
	PRIMARY KEY(id, winner, loser)
);

-- create a players standings view out of the players
-- table to be used in tournament.py
CREATE VIEW players_standings AS
SELECT *
FROM players
ORDER BY win_count DESC;