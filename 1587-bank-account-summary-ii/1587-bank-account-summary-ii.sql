-- 잔액이 10000보다 높은 사용자의 이름과 잔액을 보고하는 솔루션을 작성하세요. 
-- 계정의 잔액은 해당 계정과 관련된 모든 거래 금액의 합계와 같습니다.
select
    U.name,
    sum(T.amount) as balance
from
    Users as U
inner join
    Transactions as T
on
    U.account = T.account
group by
    U.name
having
    balance > 10000