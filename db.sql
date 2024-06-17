CREATE TABLE IF NOT EXISTS films (
    title VARCHAR(50) NOT NULL,
    gender VARCHAR(30) NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY(title)
);

INSERT INTO films (title, gender, year) VALUES ('Forest Gump', 'Drama', 1994);