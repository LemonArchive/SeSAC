use sakila;
select*
from rental;
-- [기초 조회]
-- 1. 모든 배우Actor의 이름과 성을 조회하시오.
select *
from actor;
-- 2. 배우 테이블에서 성(last_name)이 ‘DAVIS’인 사람을 모두 찾으시오.
select *
from actor 
where last_name = 'DAVIS' ;
-- 3. 고객(Customer)의 이메일 목록을 알파벳 순서로 조회하시오.
select *
from Customer  
order by email;
-- 4. 영화(film)의 제목과 대여 요금(rental_rate)을 조회하시오.
select title, rental_rate 
from film;

-- 5. 고객(Customer)의 이름, 성, 이메일을 각각 출력하시오.
select first_name, last_name , email
from customer;
-- 6. 카테고리(category)별 이름과 ID를 출력하시오.
select category_id , name
from category;
-- [조건과 정렬]
-- 7. 길이가 180분 이상인 영화 제목을 조회하시오.
select title
from film
where length >= 180;
-- 8. ‘Comedy’ 카테고리에 속한 영화 제목을 모두 조회하시오.
-- 조인 필요함

-- 9. 대여 요금이 4.99 이상인 영화 중에서 제목(title)과 요금(rental_rate)을 내림차순 정렬하시오.
select title , rental_rate
from film
where rental_rate >= 4.99
order by title desc;
-- 10. 대여(rental) 중 2005년에 이루어진 기록만 조회하시오.
select *
from rental
where rental_date like '2005%';

-- 문자열을 자르는 함수 
-- substring
select *
from rental
where substring(rental_date, 1,4) ='2005';

-- 11. 고객 중 이름이 'S'로 시작하는 고객의 이름을 조회하시오.
select *
from customer
where last_name like 'S%';
-- 12. 배우(actor) 테이블에서 이름이 5글자인 배우만 찾으시오.
select *
from actor
where last_name like '_____';

select *
from actor
where length(last_name)=5;