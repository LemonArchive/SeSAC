use world;
-- 1. 인구가 가장 많은 나라 5개의 이름과 인구를 출력하세요

select c.name ,c.Population from country c
order by c.population desc limit 5;

-- 2.대륙이 ‘Asia’인 나라들의 이름과 인구를 모두 출력하세요.
select c.name, c.Population from country c
where c.Continent = 'Asia';

-- 3.인구가 1억 이상인 나라들의 이름과 인구를 출력하세요.
select c.Name, c.Population  from country c
where Population >= 100000000;

-- 4.국민 기대수명이 80세 이상인 나라들의 이름과 기대수명을 출력하세요.
select c.name , c.LifeExpectancy from country c 
where c.LifeExpectancy >= 80;

-- 5.나라 이름이 ‘land’로 끝나는 나라의 이름을 모두 출력하세요.
select c.name from country c 
where c.name like '%land';

-- 6.인구가 500만 이상 1천만 이하인 나라들의 이름과 인구를 출력하세요.
select c.name, c.Population  from country c
where c.Population >= 5000000 and c.population <= 10000000;

-- 7.정부 형태(GovernmentForm)가 ‘Republic’인 나라들의 이름과 정부 형태를 출력하세요.
select c.name ,c.GovernmentForm  from country c
where c.GovernmentForm  = 'Republic';
-- 8.Country 테이블에서 중복 없이 대륙 이름을 모두 출력하세요.
select distinct c.Continent from country c;

-- 9.지역(Region)이 ‘Caribbean’인 나라들의 이름과 수도 번호(Capital)를 출력하세요.
select c.name,c.Capital from country c 
where c.Region = 'Caribbean'

-- 10.나라 코드(Code)가 ‘USA’, ‘BRA’, ‘FRA’ 중 하나인 나라들의 이름, 코드, 인구를 출력하세요.
select c.name,c.Code,c.Population from country c
where Code in('USA',"BRA","FRA")


