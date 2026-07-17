# 1.Install the sqlite3 module in Python and write a script to create a new database called foodie.db with a table Restaurants (id, name, cuisine, rating).

ANSWER...

IN THIS QUESTION I USE sql QUARY AND AVOID PYTHON 

```

CREATE DATABASE foodie01;
USE foodie01;

CREATE TABLE Restaurants03 (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine VARCHAR(50),
    rating DECIMAL(2,1)
);

```
# 2.Using sqlite3 in Python, insert three sample restaurants into the Restaurants table in foodie.db and write a query to fetch all restaurants with a rating above 4.0, then print their names.

ANSWER...

insert data in SQL 

```

INSERT INTO restaurants03 (id, name, cuisine, rating)
VALUES
(1, 'Pizza Hut', 'Italian', 4.5),
(2, 'Dominos', 'Italian', 4.2),
(3, 'Subway', 'American', 3.9);

```

# 3.Write Python code to load all rows from the Restaurants table in foodie.db into a Pandas DataFrame and display the top 2 rows using DataFrame.head

ANSWER...


```

SELECT *
FROM Restaurants03
LIMIT 2;


```

# 4.Add a new column 'delivery_charge' to your DataFrame, setting it to 50 for all restaurants, and then calculate a new column 'final_rating' as rating + (0.1 if cuisine is 'Italian').<br><br><em><strong>Hint:</strong> Use DataFrame.apply() or a lambda function for the conditional logic.

ANSWER...


```

SELECT *,
       50 AS delivery_charge,
       rating +
       CASE
           WHEN cuisine = 'Italian' THEN 0.1
           ELSE 0
       END AS final_rating
FROM Restaurants03;

```

# 5.Automate a daily summary: Write a Python script that connects to foodie.db, fetches all restaurants with rating above 4.5, loads them into a DataFrame, and saves the result as a CSV file named top_rated_restaurants.csv.


ANSWER...

```

SELECT *
FROM Restaurants03
WHERE rating > 4.5;

```

