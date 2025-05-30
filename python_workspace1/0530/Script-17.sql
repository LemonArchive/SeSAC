use sakila;

create or replace view v_customer as
select concat(a.last_name," ",a.first_name) as fullname
,postal_code,district,phone, location, address
from customer a
join address b on a.address_id=b.address_id;

select * from v_customer
where fullname like '%smith%';

use w3schools;
select * from orderdetails;
group by order_id;

select sum(quantity) over() from() orderdetails;
select productid, orederid, sum(quantity) over(partition by orderid) total
-- rows between
-- unbounded preceding 처음부터
-- current row 현재행
-- N preceding 현재행에서 n행이전
-- N following 현재행에서 n행이후
-- unbounded following

-- 오라클 10버젼부터 지원 -> mssql -> mysql 

-- 석차 rank()
-- quantity로 rank는 동일한 등수가 있으면
-- 건너뜀, dense_rank - 안건너뜀
select orderid, quantity,
	rank() over(order by quantity desc) as r,
	dense_rank() over(order by quantity desc) as r2
from orderdetails;

-- ntile 균등분할
select orderid, ntile(4) over() grade
from orderdetails;

-- 게시판 , primarkey로 auto_increment다넞ㅁ
-- 중간에 데이터가 삭제되었을떄 번호가 구멍이난다
-- 번호를 일시적으로 다시 붙여서 다시 보여준다
select orderid, row_number()
				over(order by orderid desc)	rnum
from orderdetails
limit 11,10;