CREATE DATABASE Snake;
USE Snake;

CREATE TABLE player_name (
    name VARCHAR (50),
    PRIMARY KEY (name)
    );
    
CREATE TABLE score_log (
	name VARCHAR (10),
    date_time VARCHAR (50),
    score INT,
    FOREIGN KEY (name) REFERENCES player_name (name)
    );

-- adding some dummy data:

INSERT INTO player_name
	(name)
VALUES
	('Billy'),
	('Mimi'),
    ('Bunty'),
    ('John'),
    ('Rita');

INSERT INTO score_log
	(name, date_time, score)
VALUES
	('Bunty', '03-05-22_13:00', 3),
	('Bunty', '03-05-22_13:02', 5),
	('Billy', '03-05-22_13:02', 1),
	('Billy', '03-05-22_13:02', 4),
	('Mimi', '03-05-22_13:02', 10),
	('Rita', '03-05-22_13:03', 8),
	('Rita', '03-05-22_13:03', 6),
	('John', '03-05-22_14:47', 15),
	('John', '03-05-22_14:49', 12);

-- CREATE VIEW for high scores (player and highest_score):

CREATE VIEW leaderboard
AS
SELECT name, MAX(score) as high_score
FROM score_log
GROUP BY name
LIMIT 10;


-- DROP database snake; 
    
    
    
   


