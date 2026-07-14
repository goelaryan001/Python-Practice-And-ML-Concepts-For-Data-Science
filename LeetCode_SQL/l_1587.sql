-- Write your PostgreSQL query statement below
SELECT
    u.name,
    COALESCE(SUM(t.amount), 0) AS balance
FROM Users u
LEFT JOIN Transactions t
    ON u.account = t.account
GROUP BY u.account, u.name
HAVING COALESCE(SUM(t.amount), 0) > 10000;