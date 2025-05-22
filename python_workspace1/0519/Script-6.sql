select title
from film A
left outer join film_category B on A.film_id=B.film_id
left outer join category C on B.category_id=C.category_id
where C.name = 'COMEDY';

-- 고객의 이름과 고객이 대여한 영화 제목을 모두 출력하자
-- customer, rental, inventory, film   
-- inventory_id, store_id, film_id
select * from inventory limit 10;
select * from customer c  limit 10;
select * from rental r   limit 10;

select concat(A.last_name, A.first_name ), D.title
from customer as A
left outer join rental B on A.customer_id = B.customer_id
left outer join inventory C on B.inventory_id = C.inventory_id
left outer join film D on D.film_id = C.film_id;

-- 문제 2 NICK WAHLNBERG 라는 배우가 출연한 영화의 제목 조회하기




select C.title
from actor as A
left outer join film_actor as B on B.actor_id = A.actor_id
left outer join film as C on C.film_id = B.film_id
where A.First_name = 'NICK'and A.last_name = 'WAHLBERG';

-- 문제3. 'London' 도시의 고객이름만 출력

select concat(A.last_name, A.first_name)
from customer as A
join address B on A.address_id = B.address_id 
join city C on B.city_id = C.city_id
where c.city ='London';

-- join 속도를 빠르게할려면, join필드에 인덱스를 만들어줘야한다.

-- 서브쿼리 : 서브쿼리는 주 쿼리 옆에서 주쿼리 보다 먼저실행되서 결과를 가져
--			온 다음에 주쿼리가 실행된다.
-- 서브쿼리는 select 절, from절, where, order by 절등 다 가능하다.
-- select 절 : 스칼라 서브 쿼리, 결과값이 null 이거나 한개만 가져오는 쿼리
-- join을 대체할 수 있따. 우리가 볼때 편해보임, 조인이 더 빠르다
-- 가급적 join으로 해결하고 join이 안될때 서브쿼리를 쓰자
use mydb; -- mydb로 사용 이동하기
-- 사원번호, 사원이름 , 부서명을 가져오라고한다
select empno, ename, deptno -- 서브쿼리를 이용해 부서명을 가져오자
from emp;
select empno, ename, deptno,
(select dname from dept where dept.deptno = emp.deptno) as dname
from emp;

select empno, ename, deptno,
(select dname from dept B where A.deptno = B.deptno) as dname
from emp A;

use sakila;

select A.first_name, A.last_name
from actor A
left outer join film_actor B on A.actor_id = B.actor_id;

select A.first_name, A.last_name ,
(select title from film C where B.film_id = C.film_id) as title
for actor A
left outer join film_actor B on A.actor_id=B.actor_id
left outer join film_actor B on A.actor_id = B.actor_id;

-- from 절에서 : 다중행을 반환한다. 다중행 서브쿼리, 인라인뷰

use mydb;

-- select * from emp where depno in(10,20)

select A.ename, dname 
from (
select * from emp where deptno in (10,20)
) as A
join dept B on A.deptno =B.deptno;


use sakila;
select A.film_id, title, length, actor_id
from film A
left outer join film_actor B on A.film_id = B.film_id;

select first_name, last_name, title
from actor A
left outer join(
select A.film_id, title, length, actor_id
from film A
left outer join film_actor B on A.film_id = B.film_id
-- inline view
) B on A.actor_id = B.actor_id;

-- where 절
use mydb;

-- emp 테이블에 SMITH 라는 사람의 부서와 같은 부서에 있는 사람들 정보

select deptno from emp where enave= 'SMITH';
--where 조건절에 오는 서브쿼리가 여러개일때
--단일행인 경우와 다중행인 경우 처리방법이 다르다.
select * from emp where deptno =20;


select * from emp 
where deptno=(select deptno from emp where ename= 'SMITH');

-- smith가 근무하는 부서의 급여 평균보다 급여를 많이받는사람들 정보를 확인하고자한다
select avg(sal) from emp where deptno = (select deptno from emp where ename='SMITH')

select ename, sal from emp
where sal > (select avg(sal) from emp where deptno= (select deptno from emp where ename='SMITH'));

-- 부서 평균 급여보다 급여가 많은 사원 조회
select * from emp
where sal > (select avg(sal) from emp);

-- 가장 높은 급여를 받는 사원 정보 조회하기
select * from emp 
where sal = (select max(sal) from emp);

-- 매니저가 존재하는 사원만 조회

select * from emp as e -- mgr 필드에 자기 상관 정보가 있다.
where e. mgr is not null;

select * from emp where mgr in(select empno from emp);
-- 나의 mgr 필드가 emp 테이블에 존재하는가

-- 상관쿼리 : 외부 쿼리의 값을 내부쿼리에서 참조하는 서브쿼리를 말한다.
-- 외부쿼리의 각 행마다 내부쿼리가 실행되는 구조
-- exists, any, all, in 등이 있다.
-- exists :  서브쿼리의 실행결과가 하나라도 있으면 True 하나도없으면 False 반환
-- 			서브쿼리의 실행결과가 한건 이라도있으면 실행된다.

-- Any - 조건을 만족하는게 하나라도 있으면 수행
--		부등호 or 부등호 or 부등호 or 부등호 or 부등호 or 부등호
-- all 모든 조건을 만족하는
--		부등호 and 부등호 and 부등호
-- in	-	등호 or 등호 or 등호 or
 
-- 부서별 평균 급여보다 높은 사원 조회
select avg(sal) from emp where deptno = 10;
select avg(sal) from emp where deptno = 20;
select avg(sal) from emp where deptno = 30;
select avg(sal) from emp where deptno = 40;

select empno, sal, deptno from emp A
where sal > (select avg(sal) from emp B where B.deptno=A.deptno);
-- 외부의 A의 deptno와 서브쿼리(내부쿼리)의 deptnor가 서로 관계가 있었다.

-- exists - 매니저가 존재하는 사원만 조회
select empno, ename,mgr from emp;alter 

select ename from emp
where mgr = 7902;

select empno, ename, mgr from emp A
where exists(
select 1 from emp B where A.mgr=B.empno);



-- 고객의 이름과 고객이 대여한 영화 제목을 모두 출력하자
-- customer, rental, inventory, film   
-- inventory_id, store_id, film_id
select * from inventory limit 10;
select * from customer c  limit 10;
select * from rental r   limit 10;

select concat(A.last_name, A.first_name ), D.title
from customer as A
left outer join rental B on A.customer_id = B.customer_id
left outer join inventory C on B.inventory_id = C.inventory_id
left outer join film D on D.film_id = C.film_id;


select concat(A.last_name, A.first_name) name, (select title from
film D where C.film_id=D.film_id) as title
from customer A
inner join rental B on  A.actor_id = B.actor_id;
inner join film C on B.film_id = C.inventory_id



-- 문제 2 NICK WAHLNBERG 라는 배우가 출연한 영화의 제목 조회하기


use sakila;

SELECT title
FROM film
WHERE film_id IN (
SELECT film_id
FROM film_actor
WHERE actor_id = (
SELECT actor_id
FROM actor
WHERE first_name = 'NICK' AND last_name = 'WAHLBERG'
  )
);
\