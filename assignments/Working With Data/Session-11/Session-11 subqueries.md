# 1.Create a SQL query using a subquery in the WHERE clause to find all restaurants from a Restaurants table whose average rating is higher than the average rating of all restaurants in the city.

ANSWER...

- A subquery in the WHERE clause is used to compare each restaurant's average rating with the overall average rating of all restaurants in the city. Only restaurants with a higher average rating than the city average are displayed.

**syntax**

```

SELECT name, average_rating
FROM Restaurants
WHERE average_rating >
(
    SELECT AVG(average_rating)
    FROM Restaurants
);

```

# 2.Write a SQL query that uses a subquery in the SELECT statement to display each user's name from a Users table along with the total number of orders they have placed from an Orders table, like a summary you might see in a Zomato user profile.

ANSWER...

- A subquery in the SELECT statement is used to display each user's name along with the total number of orders they have placed. The subquery counts the orders for each user from the Orders table.

**syntax**

```

SELECT Users.name,
       (
           SELECT COUNT(*)
           FROM Orders
           WHERE Orders.user_id = Users.id
       ) AS total_orders
FROM Users;

```

# 3.Given a Movies table and a Reviews table, write a SQL query using IN with a subquery to list all movies that have at least one review with a rating of 5 stars, as seen in BookMyShow's top-rated section.

ANSWER...


- The IN operator with a subquery is used to display all movies that have at least one review with a 5-star rating. The subquery first finds the movie IDs with a 5-star review, and the main query displays those movie names.

**syntax**

```

SELECT title FROM Movies WHERE id IN
(
    SELECT movie_id
    FROM Reviews
    WHERE rating = 5
);

```

# 4.Write a nested SQL query to find the names of all sellers from a Sellers table on a Flipkart-style platform who have sold products in every category listed in a Categories table.

ANSWER...


- A nested subquery is used to find the sellers who have sold products in every category listed in the Categories table.

**SYNTAX**

```

SELECT name FROM Sellers WHERE id IN
(
    SELECT seller_id FROM Products GROUP BY seller_id HAVING COUNT(DISTINCT category_id) = (SELECT COUNT(*)FROM Categories));

```