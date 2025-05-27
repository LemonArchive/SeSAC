-- 1. 데이터베이스 : mysql 8 넘어가면서 부터는 한글이 안깨짐
-- root 계정만 디비만들고 계정도 만들고
create database project1;

-- 계정만들기
create user 'user03'@'localhost' identified by '1234';
-- 계정에게 project1 디비에 접근할권한을 주어야한다.
grant all privileges on project1.* to 'user03'@'localhost'
