-- 홀수 번호의 아이디와 '지루하지 않은' 설명으로 동영상을 신고하는 솔루션을 작성하세요.
-- 등급별로 내림차순으로 정렬된 결과 테이블을 반환합니다.
select
    id,
    movie,
    description,
    rating
from
    Cinema
where
    description not like "boring"
    and id % 2 != 0
order by
    rating desc