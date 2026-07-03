-- Write your PostgreSQL query statement below
With cte AS
(Select customer_number, Count(order_number) as Qty
From Orders
GROUP BY customer_number)

Select customer_number
from cte
where Qty=(Select Max(Qty) From cte)

--cte is almost like a virtual view