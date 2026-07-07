select p.product_name,s.year,s.price
from Sales s
left join Product p
on s.product_id=p.pruct_id