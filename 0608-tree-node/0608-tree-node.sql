-- p_id가 null이면 Root
-- id가 p_id에 있으면 Inner
-- 모두 아니면 Leaf
select
    id,
    case 
        when p_id is null then 'Root'
        when id in (select p_id from Tree) then 'Inner'
        else 'Leaf' end as type
from
    Tree