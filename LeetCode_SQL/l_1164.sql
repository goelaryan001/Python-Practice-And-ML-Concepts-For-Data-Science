-- Write your PostgreSQL query statement below
WITH ranked AS (
    SELECT
        product_id,
        new_price,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY change_date DESC
        ) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT product_id, new_price AS price
FROM ranked
WHERE rn = 1

UNION

SELECT DISTINCT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (
    SELECT product_id
    FROM Products
    WHERE change_date <= '2019-08-16'
);