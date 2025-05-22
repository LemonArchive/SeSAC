-- emp 테이블의 정보를 확인하고 primary key 가존재하면 삭제할려고 한다
-- use mydb;
-- select * from emp limit 10;
-- desc emp;
-- select * from emp;
-- primary key 지정은 불가능하다. 이유 : empno 필드값이 이미 중복상태
-- alter table emp add constraint pk_emp primary key(empno);
-- edit - preference - sql editor - 하단에 safe updates 체크해제하고 재시작
-- 기본적을 update delete 명령을 막아놓음 
-- delete from emp where empno=8000 and ename= '장길산' ;
-- alter table emp add constraint pk_emp primary key(empno);
-- 
-- 외부키(foreign key)
-- desc dept;
-- 
-- /* 
-- alter table 테이블명
-- add constraint 외부키이르
-- foreign key(필드명)
-- references 참조테이블명(참조필드명)
-- on delete cascade -- 부모 레코드 삭제시 자식도 삭제
-- on update cascade -- 부모키값 변경시 자식도 자동으로 변경
-- 
-- */
-- 1. 참조하는 테이블(dept)의 deptno가 반드시 primary 거나 unique조건을 만족해야한다.
-- 2. 데이터 타입이 동일 해야 한다.
-- 
-- alter table emp add constraint fk_emp_dept
-- foreign key(deptno)
-- references dept(deptno);
-- 테이블 상호간에 제약조건이 발생한다.
-- select * from dept;
-- delete from dept where deptno=10; -- 외부키 떄문에 삭제 불가능하다.
-- select * from emp; 
-- 아직 홍길동에게 부서번호가 없다.
-- update emp set deptno= 5- where empno = 8000;
-- 
-- 
-- join은 inner , outer , full - ansi 표준
-- emp 테이블에는 부서번호
-- dept 테이블에는 부서번호와 부서먕
-- 두개 이상의 테이블을 하나로 붂어서 새로운 정보를 창출한다.


-- 표준조인 
-- select A.empno ,A.ename,A.deptno, b.dname
-- from emp A ,dept B
-- inner join  dept A on ondeptno=; e
se

select A.empno ,A.ename,A.deptno , b.dname
from emp A, dept B
where A. deptno=b.deptno; -- join 조건이 동일한 (equl 조건)
select A.empno ,A.ename,A.deptno , b.dname
from emp A, dept B
where A.deptno = and 
A.empno in (7369 7892, 8000,7900,7902)
-- #단점 : 조인 조건과 검색조건이 구분이 안간다. 그래서 좋ㄴ이 여러번 
-- 이루질경우에 보기안좋다.
where A.empno in (7359, 7892, 8000, 7900, 7902);

select A.empno, A.ename, deptno = B.detno
from Emp A
left outer join dept B on A.deptno b.deptno;
select distinct deptno from emp;

select * from emp;





