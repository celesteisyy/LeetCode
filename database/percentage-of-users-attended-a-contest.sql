# Write your MySQL query statement below
with c as(
    select contest_id, round((count(user_id)/3)*100 ,2)as percentage
    from register
    group by contest_id
)

select contest_id, percentage
from c
order by percentage desc, contest_id asc;