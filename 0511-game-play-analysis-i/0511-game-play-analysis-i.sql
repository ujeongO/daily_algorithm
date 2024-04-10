-- 각 플레이어의 첫 로그인 날짜를 찾아야 함
select
    player_id,
    min(event_date) as first_login
from 
    Activity
group by
    player_id