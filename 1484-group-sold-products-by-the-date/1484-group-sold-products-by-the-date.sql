-- 각 날짜별로 판매된 다양한 제품의 수와 이름을 찾는 솔루션을 작성합니다.
-- 각 날짜의 판매된 제품 이름은 사전식으로 정렬해야 합니다.
-- sell_date 순으로 정렬된 결과 테이블을 반환합니다.
select
    sell_date,
    count(distinct(product)) as num_sold,
    group_concat(distinct product order by product) as products
from
    Activities
group by
    sell_date
order by
    sell_date