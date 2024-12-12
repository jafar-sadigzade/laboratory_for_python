-- Sual: Müəllifin adı və milliyyəti ilə birlikdə orta reytinqi 9.0 və ya daha yüksək olan
-- bütün kitabları əldə etmək üçün sorğu yazın. Nəticəni kitabın adına görə sıralayın.

-- Create the Authors table
CREATE TABLE Authors
(
    author_id   INT PRIMARY KEY,
    name        VARCHAR(100),
    nationality VARCHAR(50)
);

-- Create the Books table
CREATE TABLE Books
(
    book_id        INT PRIMARY KEY,
    title          VARCHAR(150),
    author_id      INT,
    published_year INT,
    genre          VARCHAR(50),
    FOREIGN KEY (author_id) REFERENCES Authors (author_id)
);

-- Create the Reviews table
CREATE TABLE Reviews
(
    review_id INT PRIMARY KEY,
    book_id   INT,
    rating    FLOAT(2, 1
) ,
    review_text VARCHAR(255),
    reviewer_name VARCHAR(100),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Insert example data into Authors table
INSERT INTO Authors (author_id, name, nationality)
VALUES (1, 'George Orwell', 'British'),
       (2, 'Harper Lee', 'American'),
       (3, 'J.K. Rowling', 'British');

-- Insert example data into Books table
INSERT INTO Books (book_id, title, author_id, published_year, genre)
VALUES (1, '1984', 1, 1949, 'Dystopian'),
       (2, 'To Kill a Mockingbird', 2, 1960, 'Fiction'),
       (3, 'Harry Potter and the Philosopher''s Stone', 3, 1997, 'Fantasy');

-- Insert example data into Reviews table
INSERT INTO Reviews (review_id, book_id, rating, review_text, reviewer_name)
VALUES (1, 1, 9.0, 'Thought-provoking and chilling', 'Alice'),
       (2, 2, 8.5, 'A timeless classic', 'Bob'),
       (3, 3, 9.8, 'Magical and captivating', 'Charlie'),
       (4, 1, 8.7, 'A must-read for everyone', 'David');
