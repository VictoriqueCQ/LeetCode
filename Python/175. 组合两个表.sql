select FirstName, LastName, City, SState
from Person left join Address
on Person.PersonId = Address.PersonId
;
