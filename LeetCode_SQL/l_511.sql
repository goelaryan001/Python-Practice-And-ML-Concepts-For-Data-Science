select 
player_id, min(event_date) as first_login
from activity
group by player_id

SELECT DISTINCT
    player_id,
    FIRST_VALUE(event_date) OVER (
        PARTITION BY player_id
        ORDER BY event_date
    ) AS first_login
FROM Activity;