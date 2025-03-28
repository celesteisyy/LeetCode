# Write your MySQL query statement below
with first as(
    select delivery_id, customer_id, order_date, customer_pref_delivery_date, row_number() over (partition by customer_id order by order_date) as rn 
    from Delivery
)
select round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)/count(*)*100,2) as immediate_percentage
from first
where rn = 1;