# Write your MySQL query statement below
select s.product_id, min(s.year) as first_year, s.quantity, s.price
from Sales s
left join Product p on p.product_id = s.product_id
group by p.product_id;