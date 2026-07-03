-- Write your PostgreSQL query statement below
Select *, 
Case when x+y>z and y+z>x and x+z>y Then 'Yes' Else 'No' End As Triangle
from Triangle