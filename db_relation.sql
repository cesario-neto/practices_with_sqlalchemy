CREATE TABLE IF NOT EXISTS films (
    title VARCHAR(50) NOT NULL,
    gender VARCHAR(30) NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY(title)
);

CREATE TABLE IF NOT EXISTS actors (
    id SERIAL NOT NULL,
    name VARCHAR(50) NOT NULL,
    film_title VARCHAR(50) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (film_title) REFERENCES films(title)
);

INSERT INTO films (title, gender, year)
VALUES ('Forest Gump', 'Drama', 1994);

INSERT INTO actors (name, film_title)
VALUES ('Tom Hanks', 'Forest Gump');