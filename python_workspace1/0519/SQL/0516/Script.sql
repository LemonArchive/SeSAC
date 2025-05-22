use sakila;
select * from customer;
-- 1. film 테이블에서 영화 제목과 대여 요금을 조회하시오.
select f.title, f.rental_rate 
from film f; 

-- 2. actor 테이블에서 이름이 'JOHN'인 배우를 조회하시오.
select a.*
from  actor a 
where a.first_name ="JOHN";
-- 3. category 테이블의 모든 카테고리 이름을 조회하시오.
select name 
from category ;
-- 4. film 테이블에서 rental_rate가 3.99보다 큰 영화의 제목과 요금을 조회하시오.
select f.title , f.rental_rate 
from film f
where f.rental_rate > 3.99

-- 5. customer 테이블에서 이메일 주소에 'gmail'이 포함된 고객을 조회하시오.
select c.*
from customer c
where c.email like 'gmail%';
-- 6. film 테이블에서 길이가 120분 이하인 영화의 제목과 길이를 조회하시오.
select f.title, f.length 
from film f
where f.`length` <= 120;
-- 7. language 테이블에서 언어 이름이 'English'인 행을 조회하시오.
select l.*
from language l 
where l.name = "English";
-- 8. actor 테이블에서 성(last_name)이 'SMITH'인 배우의 이름과 성을 조회하시오.
select a.first_name ,a.last_name
from actor a
where a.last_name = 'SMITH';
-- 9. customer 테이블에서 first_name이 'A'로 시작하는 고객을 조회하시오.
select c.*
from customer c
where c.first_name like 'A%';
-- 10. film 테이블에서 2006년에 개봉한 영화만 조회하시오.
select f.*
from film f
where SUBSTRING(release_year, 1,4) = 2006;
-- 11. 배우 번호가 10,21,34,56,87,89,90인 사람들 정보만출력
select a.*
from actor a
where a.actor_id in (10,21,34,56,87,89,90);

-- 12. customer 테이블중에서 store_Id=1 이고 customer_id가 562,580,470,471,363,364 
select c.*
from customer c
where c.store_id = 1 and customer_id in (562,580,470,471,363,364);