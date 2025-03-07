# Write your MySQL query statement below
with a as(
    select count(distinct(subject_id)) as num_unique_sub, dept_id, teacher_id
    from Teacher
    group by dept_id, teacher_id
)
select teacher_id, num_unique_sub as cnt
from a
group by teacher_id;