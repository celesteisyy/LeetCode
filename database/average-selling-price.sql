# Write your MySQL query statement below
select p.product_id, IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units),2),0) AS average_price
from Prices p
left join UnitsSold u on p.product_id = u.product_id
where u.purchase_date between p.start_date and p.end_date
group by u.product_id;