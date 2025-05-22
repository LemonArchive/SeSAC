-- emp 테이블의 내용을 다 보여줌 - 14
select * from emp;

-- 데이터 전체 몇건인가?
select count(*) from emp;

-- * :아스테리스크 모든 필드
select empno,ename,job from emp;

-- ailasing 0 별명 테이블명을 수정해서 부를 수 있다.
select empno, ename, job
from emp as e;

-- information_schema 디비에 사용자가 만드는 테이블
-- 정보가 저장된다. ailasing 안쓰면 저 디비 다 검색해서
-- 정보를 읽어오고 ailasing을 하면 캐시를해서
-- 디비정보를 메모리에 불러놓고 작업 속도에서 유리함  
select e.empno, e.ename, e.job
from emp as e;

-- as 생략가능 count(필드명)  dbms는 null 값
-- 이 있을경우 카운트안함
-- count(*) - 필드중에 null값이 아예 없는 필드를 기준으로
-- 			제일 많은 데이터를 카운트를 가져와라
select count(e.sal) from emp e;

/* 
null 값? 알수없는 , 파이썬의 None , 수학적으로 무한대의 의미를 갖는다
null + 1 => null (무한대)
null - 1 => null (무한대)

수학연산 다 가능 (+, -, *, /, sin, cosin, tan, round ......)  
null값에  결과는 null
파이썬의 if 문 , 함수 써서 처리가능
DBMS 의 쿼리는 ANSI 표준이 있어서 비슷한데 함수는 각자 다르다
NVL - 오라클 , ISNULL, IFNULL 

IFNULL(필드명, 기본값) 만일 필드명에서 값이 NULL 이 아닌 값이오면그 값을 주고
NULL이면 기본값을 부여한다.
*/
SELECT EMPNO, SAL, COMM, SAL+IFNULL(COMM, 0) as total_sal
FROM EMP;

-- 홍길동의 급여는 얼마입니다.
select concat(ename, "님의 급여는", sal,"입니다") as title
from emp;
-- 조건절`
/*
select 필드들
from 테이블명
where 조건절 해당조건에 만족하는 데이터
			= != >  <  >= <=
			논리연산자 and, or not
            
*/
select * from emp;
-- 이름이 smith인 사람만 보려고 한다.
select * from emp where ename='SMITH';
select * from emp where ename='smith';

-- 이름이 smith 이거나 ford 인 사람
select * from emp where sal  'SMITH' or ename = 'FORD';

select * from emp where sal >= 3000;

select * from emp where job = 'manager';
select * from emp where sal between 5000 and 2000; 
select * from emp where comm is not NULL;
select * from emp where ename like 'A%';
-- % 이건 A ~~~ 글자수제한없음 A__ 요건 _숫자만큼 글자있는애들만
select * from emp where deptno in(10,20,30);
-- 나열해서 찾아야 할 경우 -> in 연산자 오라클 500개까지가능
select empno
from emp
where empno in(7521, 7565,7903,7934);e


select * from emp where hiredate < 1981
-- order by (desc) ename; -- 이름으로 오름차순
