select
    firstName,
    lastName,
    city,
    state
from
    Person as P
Left join
    Address as A
On
    p.personId = A.personId