use mydb2;
-- 스타디움, 스케쥴 홈팀이김 어웨이팀이김
select s.stadium_name,sc.sche_date, sc.HOME_SCORE, sc.AWAY_SCORE,
case
	when sc.HOME_SCORE = sc.AWAY_SCORE then '무승부'
	when sc.HOME_SCORE > sc.AWAY_SCORE then '홈팀승리'
	else '어웨이팀 승리'
end as '승부'
case
	when sc.HOME_SCORE > sc.AWAY_SCORE then sc.hometeam_id
	when sc.HOME_SCORE < sc.AWAY_SCORE then sc.awayteam_id 
	else '없음'	
end as 'winner'
from schedule sc
join stadium s on sc.stadium_Id = s.stadium_id;

use mydb;
drop table tb_guestbook;
create table tb_guestbook
-- mysql의 auto_increment mssql의 일련번호
-- 오라클은 시퀸스
-- mysql 에서 auto_increment 속성은 테이블에 하나의 필드만 
-- 반드시 primary key 여야한다.
(
	id bigint auto_increment primary key,
	title varchar(1000) not null,
	contents text,
	writer bigint, -- tb_member와 foreign key로 무 ㄲ음
	regdate datetime
);

show tables;

-- 외래키 tb_guestbook이 tb_member 참조하는 구조이다.
alter table tb_guestbook
add constraint fk_guestbook_member
foreign key (writer)
references tb_member(member_id);

-- information_schema, mysql , performance_schema
-- 시스템 데이터베이스 : 시스템이 운영한다

use information_schema;

select table_name 
from tables
where table_schema='sakila';


select *
from key_column_usage
where table_schema='mydb2';
alter table tb_guestbook
drop foreign key fk_guestbook_member;

alter table tb_guestbook
add constraint fk_guestbook_member
foreign key (writer)
references tb_member(member_id);

select 
insert into tb_guestbook (title, writer, contents,regdate)
values('제목1', 1, '내용1', now())

insert into tb_guestbook (title, writer, contents,regdate)
values('제목2', 2, '내용2', now())