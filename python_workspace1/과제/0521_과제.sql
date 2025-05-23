use sakila;

-- 1. 모든 배우(actor) 정보를 조회하세요. 다음처럼 출력이 나오게 하세요
-- +----------------------+
-- | 배우이름             |
-- +----------------------+
-- | GUINESS PENELOPE     |
-- | WAHLBERG NICK        |
-- | CHASE ED             |
-- | DAVIS JENNIFER       |
-- | LOLLOBRIGIDA JOHNNY  |
-- | NICHOLSON BETTE      |
-- | MOSTEL GRACE         |
-- | JOHANSSON MATTHEW    |
-- | SWANK JOE            |
-- | GABLE CHRISTIAN      |
-- | CAGE ZERO            |
-- | BERRY KARL           |
-- | WOOD UMA             |
-- | BERGEN VIVIEN        |
-- .........................  이하생략 

select concat(a.last_name ,' ', a.first_name) as actor
from actor a 
limit 20;

-- 2. 성(last_name)이 'BERRY', 'HOFFMAN', 'DENCH' 인 배우를 조회하세요.  or연산자로 한번 in 연산자로 한번 두번 작성해보세요
 
select a.*
from actor a 
where a.last_name in ('BERRY','HOFFMAN','DENCH') ;

select a.*
from actor a 
where a.last_name = 'BERRY' or a.last_name = 'HOFFMAN'or a.last_name ='DENCH';

-- 3. 이름이 'SCARLETT'인 배우의 actor_id를 조회하세요.

select a.actor_id
from actor a 
where a.first_name  = 'SCARLETT';

-- 4. actor_id가 2,18,34,56,77,88,120, 199, 192, 191 인 배우의 정보를 조회하시오 출력방식은 1번 참조입니다.

select concat(a.last_name ,' ', a.first_name) as actorname
from actor a 
where a.actor_id in ('2', '18', '34', '56', '77', '88', '120','199','192','191');

-- 5.고객(customer) 테이블에서 이메일이 'KATHLEEN.ADAMS@sakilacustomer.org'인 고객의 전체 정보를 조회하세요.

select c.*
from customer c
where c.email = 'KATHLEEN.ADAMS@sakilacustomer.org';

-- 6. 고객 중에서 store_id가 1이고 last_name이 'MILLER'인 사람을 조회하세요.

select c.*
from customer c
where c.store_id = 1 and c.last_name = 'MILLER';

-- 7. 카테고리(category) 이름이 'Comedy'인 카테고리의 ID를 찾으세요.

select c.category_id
from category c
where c.name = 'Comedy';

-- 8. 7일 이상 대여된(rental_duration > 7) 영화 정보를 조회하세요.

select f.*
from film f
where f.rental_duration > '7'; -- 7일 '이상' 대여된인데 (rental_duration > 7)....?

select *
from film f 
where f.rental_duration >= '7';

-- 9. replacement_cost가 20 이상 25 이하인 영화 목록을 조회하세요.
select *
from film f
where f.replacement_cost >= '20' and f.replacement_cost <= '25';  -- 둘다가능

select *
from film f
where f.replacement_cost between '20' and '25';  -- 둘다가능
 
-- 10. title에 'ACADEMY'라는 단어가 포함된 영화 제목만 검색하세요.

select f.title
from film f 
where title like '%ACADEMY%';

-- 11. 가장 최근에 등록된 고객 5명의 이름과 이메일을 조회하세요.
select concat(c.last_name,c.first_name) as customername ,c.email
from customer c 
order by c.create_date desc 
limit 5;

-- 12. 'Comedy' 카테고리에 속한 모든 영화 제목을 조회하세요.

select f.title
from film f
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id 
where c.name = 'Comedy';

-- 13. 고객과 대여(rental)를 조인하여 고객 이름과 대여 일자를 10건만 조회하세요.

select concat(c.last_name,c.first_name) as customername, r.rental_date
from customer c
join rental r on c.customer_id = r.customer_id
limit 10;

-- 14. 'Action' 장르의 영화를 빌린 고객 이름과 영화 제목을 조회하세요.

select concat(c.last_name,c.first_name) as customername, f.title
from film f
join film_category fc on f.film_id = fc.film_id
join category ca on fc.category_id = ca.category_id 
join inventory i on f.film_id  = i.inventory_id
join rental r on i.inventory_id = r.inventory_id
join customer c on r.customer_id = c.customer_id
where ca.name = 'Action';

-- 15. 'Alberta'에 사는 고객의 이름과 이메일을 조회하세요.
select concat(c.last_name,c.first_name) as customername,c.email,c.address_id
from customer c 
join store s on c.address_id  = s.address_id
join address a on s.address_id = a.address_id
join city ct on a.city_id = ct.city_id
where district = 'Alberta'; 

-- 16. 배우 이름과 그 배우가 출연한 영화 제목을 전체에서 10건만 조회하세요.
select concat(a.last_name,' ',a.first_name) as actorname, f.title
from actor a 
join film_actor fa  on a.actor_id = fa.actor_id
join film f on fa.film_id = f.film_id 
limit 10;
-- 17. 각 고객이 대여한 총 횟수를 고객 이름과 함께 조회하세요

select concat(c.last_name,' ',c.first_name) as customername , COUNT(r.customer_id) as cnt
from customer c
join rental r on c.customer_id = r.customer_id 
group by r.customer_id

-- 18. 각 배우가 출연한 영화 수를 조회하고, 가장 많이 출연한 배우 상위 5명을 조회하세요.

select concat(a.last_name,' ',a.first_name) as actorname,  COUNT(fa.actor_id) as cnt 
from actor a 
join film_actor fa  on a.actor_id = fa.actor_id
group  by fa.actor_id 
order by cnt desc
limit 5;

-- 19. 각 스토어별로 총 매출을 조회하세요.

 select sum(p.amount) as amo, 
 case 
	 when s.store_id = '1' then '오늘의 밥상'
	 when s.store_id = '2' then '내일의 밥상'
  end as 'storename'  -- store_id밖에없어서 이름지어줌
 from store s 
 join staff stf on s.store_id = stf.store_id
 join payment p on stf.staff_id = p.staff_id
 group by s.store_id ; 
 
 
 -- 20. 월별 대여 건수를 조회하세요 (예: 2005-06, 2005-07 등)
 
 select DATE_FORMAT(r.rental_date, '%Y-%m') as month,
 COUNT(r.rental_date) as '대여 횟수'
 from rental r
 group by month
 