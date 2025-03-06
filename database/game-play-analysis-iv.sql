# Write your MySQL query statement below
select round(sum(consec_login) / count(distinct player_id), 2) as fraction
FROM (select player_id, datediff(event_date, min(event_date) over (partition by player_id)) = 1 as consec_login
    from Activity) as t;