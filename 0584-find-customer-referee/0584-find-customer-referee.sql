-- id가 2인 회원이 추천하지 않은 customer의 이름 반환
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL