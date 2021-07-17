DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    matches INT,
    points INT,
    goals_for INT,
    goals_against INT
);