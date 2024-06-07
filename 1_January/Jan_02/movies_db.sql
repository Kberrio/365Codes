CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    director TEXT,
    year_released INTEGER,
    genre_id INTEGER,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

CREATE TABLE genres (
    genre_id INTEGER PRIMARY KEY,
    genre_name TEXT NOT NULL
);

INSERT INTO genres (genre_name) VALUES ('Action'), ('Comedy'), ('Drama'), ('Fantasy'), ('Horror');

INSERT INTO movies (title, director, year_released, genre_id) VALUES 
('Inception', 'Christopher Nolan', 2010, (SELECT genre_id FROM genres WHERE genre_name = 'Action')),
('The Grand Budapest Hotel', 'Wes Anderson', 2014, (SELECT genre_id FROM genres WHERE genre_name = 'Comedy')),
('Parasite', 'Bong Joon-ho', 2019, (SELECT genre_id FROM genres WHERE genre_name = 'Drama'));

SELECT * FROM movies;

SELECT m.title, m.director, m.year_released, g.genre_name 
FROM movies m
JOIN genres g ON m.genre_id = g.genre_id
WHERE g.genre_name = 'Comedy';

UPDATE movies SET year_released = 2015 WHERE title = 'The Grand Budapest Hotel';

DELETE FROM movies WHERE title = 'Parasite';

