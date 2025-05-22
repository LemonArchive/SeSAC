use w3schools;

-- 1.주문이 한번도 없는 고객의 이름을 조회하기

select C.CustomerName 
from customers C
LEFT OUTER join orders O on C.CustomerID = O.CustomerID 
where orderid is null;

-- 2.가장 주문건수가많은 판매자 이름 구하기

select concat(A.FirstName,' ',A.LastName)
from employees A
left outer join orders B on A.EmployeeID = B.EmployeeID 
group by A.EmployeeID ,A.FirstName,A.LastName
order by count(b.orderid) desc
limit 1;

-- 3.판매건수가 5개 이상인 판매자의 인원수

select count(*) as seller
from (
select A.EmployeeID
from employees A
left outer join orders B on A.EmployeeID = B.EmployeeID 
group by A.EmployeeID
having count(b.orderid) >= 5
) as sb;