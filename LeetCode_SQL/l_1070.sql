with cte as(
select product_id, min(year) as first_year
from Sales
group by product_id
)
select s.product_id, s.year as first_year, s.quantity, s.price
from Sales s
inner join cte
aon s.product_id=cte.product_id
and s.year=cte.first_year


with cte as(select
product_id, 
year,
first_value(year) over (partition by product_id order by year) as first_year,
quantity, price
from Sales)

select product_id, 
first_year,
quantity, price
from cte where year=first_year