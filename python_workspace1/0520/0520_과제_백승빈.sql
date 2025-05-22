-- 오늘의 과제
use w3schools;
-- 1. customers 테이블에서 나라가 Germany인 나라의 정보 전체
select c.*
from customers c
where c.Country ='Germany';
-- 2. customers 테이블에서 나라가 Austria,USA,Poland,Denmark 에 사는 고객리스트
select c.CustomerName 
from customers c
where c.Country in ('Austria','USA','Poland','Denmark');
-- 3. 각자 나라별로 고객이 몇명씩 있는지 확인 
select country ,count(c.customerId) as '고객수'
from customers c 
group by Country ;
-- 4. 나라별로 고객이 5명이상이나라목록
select c.Country
from customers c 
group by c.Country ㅐㅐ
having count(c.customerId) >= 5;
-- 5. 나라이름이 B로 시작하는 나라들의 고객전체합
select COUNT(*)
from customers c 
where c.Country like 'B%';
-- 6. 나라는 UK 도시명은 London에 있는 고객들 이름목록
select c.CustomerName
from customers c 
where Country = "UK" and City = 'London';
-- 7. 주문일이 '1996-07-01 '~' 1996-09-30' 일까지의 주문아이디와 고객이름
select o.orderid,c.CustomerName
from Customers c
inner join orders o on c.Customerid = o.CustomerID
where o.OrderDate > '1996-07-01' and o.OrderDate < '1996-09-30';
-- 8. 위의 7번 문제를 고객이름 오름차순으로 정렬하여 출력하기
select o.orderid,c.CustomerName
from Customers c
inner join orders o on c.Customerid = o.CustomerID
where o.OrderDate > '1996-07-01' and o.OrderDate < '1996-09-30'
order by c.customerName ASC;
-- 9. 배달자가 Federral Shipping 인경우의 상품명 가격 수량 만
select p.productName,p.price,d.quantity
from orders o 
inner join orderdetails d on o.OrderID    = d.orderID
inner join products     p on d.ProductID  = p.ProductID
inner join shippers     s on o.ShipperID  = s.ShipperID 
where s.ShipperName = 'Federal Shipping';