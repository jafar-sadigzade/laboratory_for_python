-- Query to find big countries -- for lab2/task1
SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;


-- Query to find movies with odd-numbered IDs and descriptions that are not "boring" -- for lab2/task2
SELECT id, movie, description, rating
FROM Cinema
WHERE MOD(id, 2) = 1
  AND description != 'boring'
ORDER BY rating DESC;

-- for lab2/task3
SELECT b.title, a.name AS author_name, a.nationality, AVG(r.rating) AS average_rating
FROM Books b
         JOIN Authors a ON b.author_id = a.author_id
         JOIN Reviews r ON b.book_id = r.book_id
GROUP BY b.book_id, a.name, a.nationality
HAVING AVG(r.rating) >= 9.0
ORDER BY b.title;
