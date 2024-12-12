-- Create the Cinema table
CREATE TABLE Cinema
(
    id          INT PRIMARY KEY,
    movie       VARCHAR(100),
    description VARCHAR(255),
    rating      FLOAT(3, 1)
);

-- Insert example data into the Cinema table
INSERT INTO Cinema (id, movie, description, rating)
VALUES (1, 'War', 'great 3D', 8.9),
       (2, 'Science', 'fiction', 8.5),
       (3, 'irish', 'boring', 6.2),
       (4, 'Ice song', 'Fantacy', 8.6),
       (5, 'House card', 'Interesting', 9.1);


