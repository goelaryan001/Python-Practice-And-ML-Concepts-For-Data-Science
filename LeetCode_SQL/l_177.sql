CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    with cte as(
    select 
    e.salary,
    dense_rank() over(order by e.salary desc) as rnk
    from Employee e)
    select distinct c.salary 
    from cte c
    where c.rnk=N
  
  );
END;
$$ LANGUAGE plpgsql;

