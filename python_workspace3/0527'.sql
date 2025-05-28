-- 1. 데이터베이스 : mysql 8 넘어가면서 부터는 한글이 안깨짐
-- root 계정만 디비만들고 계정도 만들고
create database project1;
use project1;

-- 계정만들기
create user 'user03'@'localhost' identified by '1234';
-- 계정에게 project1 디비에 접근할권한을 주어야한다.
grant all privileges on project1.* to 'user03'@'localhost'

-- 회원테이블 
drop table tb_member;
create table tb_member(
	-- mysql은 auto_increment 속성있는 필드가 무조건 primary key가 되어야 한다.
	member_id bigint auto_increment primary key,
	user_id varchar(40),
	password varchar(300), -- md5 암호화 알고리즘등 암호화하면 글자수가늘어남
						  -- 저장, 
	user_name varchar(40), 
	email varchar(40),
	phone varchar(40),
	regdate datetime
);
	
-- 게시판테이블

insert into tb_member(user_id, password, user_name,
email, phone, regdate) 
values('test1','1234','홍길동','hong@google.com','010-0000-0001', now());



create table tb_score(
	id bigint primary key auto_increment,
	sname varchar(20) not null,
	kor int not null,
	eng int not null,
	mat int not null,
	regdate datetime);
