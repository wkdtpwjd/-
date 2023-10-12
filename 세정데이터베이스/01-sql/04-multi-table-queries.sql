-- scott.sql 을 이용해서 join연습

--article,user 같이 조회
SELECT *
 FROM article ,user
WHERE article.userid = user.id;


--EMPLOYEE, DEPARTMENT
SELECT * 
 FROM EMPLOYEE e,DEPARTMENT d
WHERE e.deptno = d.deptno;

--동등조인 ==INNER JOIN => 양쪽다 같은 값을 가지고있어야 조회가됨
SELECT *
 FROM EMPLOYEE e
 INNER JOIN DEPARTMENT d
  ON e.deptno = d.deptno;


--각 직원의 상사 이름을 조회
SELECT e1.name,e1.job,e1.deptno,e1.boss,e2.name
 FROM EMPLOYEE e1,EMPLOYEE e2
 WHERE e1.boss = e2.empno;

SELECT * FROM EMPLOYEE;


-- 한쪽이라도 값을 가지고 있으면 일단 조회
-- 하고 없는 쪽은 NULL표시하면 좋겠는데..?
-- LEFT (OUTER)생략가능 JOIN

SELECT e1.name,e1.job,e1.deptno,e1.boss,e2.name
 FROM EMPLOYEE e1
 LEFT OUTER JOIN EMPLOYEE e2
  ON e1.boss = e2.empno;


--직원의 이름 상사이름 부서이름 조회 (테이블 3개조회)
SELECT e1.name,e2.name,d.name
 FROM EMPLOYEE e1, EMPLOYEE e2,DEPARTMENT d
 WHERE e1.boss = e2.empno
 AND e1.deptno = d.deptno;
