WITH cte AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
),
cte2 AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)
SELECT ROUND(SUM(i.tiv_2016)::numeric, 2) AS tiv_2016
FROM Insurance i
JOIN cte c
    ON i.tiv_2015 = c.tiv_2015
JOIN cte2 c2
    ON i.lat = c2.lat
   AND i.lon = c2.lon;

