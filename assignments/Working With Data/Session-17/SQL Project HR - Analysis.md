# 1.Create a SQL table called Restaurant with columns: id, name, cuisine, location, and average_rating. Insert at least 5 sample rows representing popular restaurants from Zomato.

ANSWER...


```

CREATE TABLE Restaurant (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine VARCHAR(50),
    location VARCHAR(100),
    average_rating DECIMAL(2,1)
);

INSERT DATA

INSERT INTO Restaurant (id, name, cuisine, location, average_rating)
VALUES
(1, 'Barbeque Nation', 'North Indian', 'Ahmedabad', 4.4),
(2, 'Dominos Pizza', 'Italian', 'Rajkot', 4.2),
(3, 'Pizza Hut', 'Italian', 'Surat', 4.3),
(4, 'McDonalds', 'Fast Food', 'Vadodara', 4.1),
(5, 'The Grand Thakar', 'Gujarati', 'Rajkot', 4.6);

```


# 2.Write a SQL query to generate a report showing the number of restaurants for each cuisine type from your Restaurant table, ordered by the count in descending order.

ANSWER..


```
SELECT
    cuisine,
    COUNT(id) AS total_restaurants
FROM Restaurant
GROUP BY cuisine
ORDER BY total_restaurants DESC;

```

# 3.Add a new table called Review with columns: id, restaurant_id, user_name, rating, and review_date. Insert at least 10 sample reviews linking them to restaurants using restaurant_id.


ANSWER...

CREAT TABLE

```

CREATE TABLE Review (
    id INT PRIMARY KEY,
    restaurant_id INT,
    user_name VARCHAR(100),
    rating DECIMAL(2,1),
    review_date DATE,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(id)
);

```
INSERT DATA

```

INSERT INTO Review (id, restaurant_id, user_name, rating, review_date)
VALUES
(1, 1, 'Amit', 4.5, '2026-07-01'),
(2, 1, 'Rahul', 4.3, '2026-07-02'),
(3, 2, 'Priya', 4.2, '2026-07-03'),
(4, 2, 'Neha', 4.0, '2026-07-04'),
(5, 3, 'Karan', 4.6, '2026-07-05'),
(6, 3, 'Riya', 4.4, '2026-07-06'),
(7, 4, 'Vijay', 4.1, '2026-07-07'),
(8, 4, 'Anjali', 4.3, '2026-07-08'),
(9, 5, 'Sanjay', 4.8, '2026-07-09'),
(10, 5, 'Pooja', 4.7, '2026-07-10');

```

# 4.Write a SQL query using a JOIN to display each restaurant's name, cuisine, and its average review rating (from the Review table), ordered by the highest average rating first.

ANSWER..

```

SELECT
    r.name,
    r.cuisine,
    AVG(rv.rating) AS average_review_rating
FROM Restaurant r
JOIN Review rv
ON r.id = rv.restaurant_id
GROUP BY r.id, r.name, r.cuisine
ORDER BY average_review_rating DESC;

```

# 5.5. Use a window function to rank restaurants by their average review rating within each cuisine type, showing the restaurant name, cuisine, average rating, and rank.

ANSWER..

```

SELECT
    r.name,
    r.cuisine,
    AVG(rv.rating) AS average_rating,
    RANK() OVER (
        PARTITION BY r.cuisine
        ORDER BY AVG(rv.rating) DESC
    ) AS restaurant_rank
FROM Restaurant r
JOIN Review rv
ON r.id = rv.restaurant_id
GROUP BY r.id, r.name, r.cuisine;

```
