# Write your MySQL query statement below
select product_id, year as first_year, quantity, price
from (select s.*, rank() over (partition by product_id order by year) as rn
        from Sales s
        ) as t
where rn = 1;
