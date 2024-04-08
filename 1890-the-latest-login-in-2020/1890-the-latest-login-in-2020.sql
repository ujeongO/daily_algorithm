-- 2020년에 로그인한 user_id 반환 
-- 2020년에 여러번 로그인 했다면 가장 최근 결과를 반환
select
    user_id,
    max(time_stamp) as last_stamp
from
    Logins
where
    year(time_stamp) = 2020
group by
    user_id