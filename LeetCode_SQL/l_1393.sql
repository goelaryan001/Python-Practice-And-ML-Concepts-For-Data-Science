select stock_name, Sum(Case when oprations='Buy' then price*-1 else price end) as capital_gain_loss
from Stocks
group by stock_name