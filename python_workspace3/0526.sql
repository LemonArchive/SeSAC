use mydb;
select * from emp;
delete from emp where empno=8005;
select * from emp;

start transaction;
delete from emp;
select * from emp;
rollback; -- 트랜잭션롤백

-- 계정만들기 
-- localhost - 루프백주소(127.0.0.1)
drop user 'user02'@'localhost'
create user 'user02'@'localhost'
identified by 'qwer';
grant all privileges on mydb.* to 'user02'@'localhost'

desc emp;
create table tb_score(
	id bigint primary key auto_increment,
	sname varchar(20) not null,
	kor int not null,
	eng int not null,
	mat int not null,
	regdate datetime);

insert into tb_score(sname,kor,eng,mat,regdate)
values('홍길동',90,90,90, now());

select sname, kor,eng,mat,
(kor+eng+mat) as total,
date_format(regdate, '%Y-^m-d %H:%i:%s') regdate
from tb_score;


-- 전체보기
-- 추가 : 입력받아서
-- 수정
-- update 테이블명 set 필드1='값1', 필드2='값2' where절
-- 삭제
-- delete from 테이블명 where id=1
-- 검색

create table week_pay(
	id bigint primary key auto_increment,
	sname varchar(20) not null,
	worktime int not null,
	perpay int not null,
	regdate datetime
	);

SELECT id, sname, worktime, perpay,(worktime*perpay) as total,
case 
when worktime > 20
then (worktime*perpay) + (worktime - 20) * perpay * 0.5
end as overpay
FROM week_pay;
    
