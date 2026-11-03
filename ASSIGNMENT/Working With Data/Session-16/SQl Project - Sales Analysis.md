# 1.Import a CSV file of food delivery orders (with columns like order_id, restaurant_name, customer_name, order_amount, order_date) into a new SQL table named FoodOrders using your database tool of choice.

ANSWER...

write a SQl quary

```

CREATE TABLE FoodOrders (
    order_id INT PRIMARY KEY,
    restaurant_name VARCHAR(100),
    customer_name VARCHAR(100),
    order_amount DECIMAL(10,2),
    order_date DATE
);

```

# 2.Write SQL statements to create a table called TopSongs with columns: song_id, song_title, artist, streams, and release_date, then insert at least 5 records representing popular tracks from Spotify.

ANSWER...

```
CREATE TABLE TopSongs (
    song_id INTAUTO_INCREMENT PRIMARY KEY,
    song_title VARCHAR(100),
    artist VARCHAR(100),
    streams BIGINT,
    release_date DATE
);

DATA INSEART 


INSERT INTO TopSongs (song_id, song_title, artist, streams, release_date)
VALUES
(1, 'Blinding Lights', 'The Weeknd', 4200000000, '2019-11-29'),
(2, 'Shape of You', 'Ed Sheeran', 3900000000, '2017-01-06'),
(3, 'Someone You Loved', 'Lewis Capaldi', 3100000000, '2018-11-08'),
(4, 'As It Was', 'Harry Styles', 2800000000, '2022-04-01'),
(5, 'Levitating', 'Dua Lipa', 2600000000, '2020-03-27');


```


# 3.Using SQL, calculate the total amount spent by each customer and display the top 3 customers based on total spending.


ANSWER...

```
SELECT
    customer_name,
    SUM(order_amount) AS total_spent
FROM FoodOrders
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 3;

```

# 4.Write a SQL query to generate a restaurant performance report showing the total number of orders and total order amount for each restaurant.

ANSWER...


```


SELECT
    restaurant_name,
    COUNT(order_id) AS total_orders,
    SUM(order_amount) AS total_order_amount
FROM FoodOrders
GROUP BY restaurant_name
ORDER BY total_order_amount DESC;


```


# 5.Create a SQL query that returns two KPIs:
- Average Order Amount
- Number of Unique Customers


ANSWER...


```


SELECT
    AVG(order_amount) AS average_order_amount,
    COUNT(DISTINCT customer_name) AS unique_customers
FROM FoodOrders;

```

