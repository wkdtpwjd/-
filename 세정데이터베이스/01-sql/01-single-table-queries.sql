-- 01. Querying data --는 :주석의미
SELECT
 LastName
FROM
 employees;

SELECT
 LastName,FirstName
FROM
 employees;

SELECT
 *
FROM
 employees;

SELECT
 FirstName AS '이름'
FROM
 employees;

SELECT
 Name,Milliseconds/60000 
FROM
 tracks;

SELECT
 Name,Milliseconds/60000 AS '재생시간(분)'
FROM
 tracks;

-- 02. Sorting data
SELECT
 FirstName 
FROM
 employees
ORDER BY
 FirstName; --오름차순정렬 뒤에 ASC붙여도 결과는 동일

SELECT
 FirstName 
FROM
 employees
ORDER BY
 FirstName DESC; --내림차순 정렬

SELECT
 FirstName 
FROM
 employees
ORDER BY
 FirstName DESC;

SELECT
 Country, City
FROM
 customers
ORDER BY
 Country DESC,  --컨트리 기준으로 먼저 내림차순 해서
 City ASC;      --같은 컨트리 기준안에서 city가 오름차순 정렬됨

SELECT
 Name,Milliseconds /60000 AS '재생시간(분)'
FROM
 tracks
ORDER BY
 Milliseconds DESC;
 


-- NULL 정렬 예시

SELECT
 ReportsTo
FROM
 employees
ORDER BY
 ReportsTo;   -- NULL이 가장 먼저 출력


-- 03. Filtering data
SELECT DISTINCT -- 국가하나만 남기고 중복제거해라 
 Country
FROM
 customers
ORDER BY
 Country;   --각 국가를 오름차순 출력

SELECT
 LastName,FirstName,City
FROM
 customers
WHERE 
 City = 'Prague'; -- 프라하인것 출력


SELECT
 LastName,FirstName,City
FROM
 customers
WHERE 
 City != 'Prague'; --프라하아닌것 출력


SELECT
 LastName,FirstName,Company,Country
FROM
 customers
WHERE 
 Company = NUll,  -- '='으로 NULL판별불가
 AND Country = 'USA';


SELECT
 LastName,FirstName,Company,Country
FROM
 customers
WHERE 
 Company IS NUll
 AND Country = 'USA';

SELECT
 LastName,FirstName,Company,Country
FROM
 customers
WHERE 
 Company IS NUll
 OR Country = 'USA';

SELECT
 Name,Bytes
FROM
 tracks
WHERE 
 100000 <= Bytes <= 500000;
-- 위의식은 두개의 범위를 지정할수 없다

SELECT
 Name,Bytes
FROM
 tracks
WHERE 
Bytes BETWEEN 100000 AND 500000;
-- BETWEEN사용 또는 AND로 이어 적기 

SELECT
 Name,Bytes
FROM
 tracks
WHERE 
 Bytes BETWEEN 100000 AND 500000
ORDER BY
 Bytes;
 -- ORDER BY랑 WHERE순서 바꾸면 값출력안됨! 순서중요

SELECT
 LastName,FirstName,Country
FROM
 customers
WHERE 
 Country = 'Canada'
 OR Country = 'Germany'
 OR Country = 'France'; --결과는 맞게나옴

SELECT
 LastName,FirstName,Country
FROM
 customers
WHERE 
 Country IN ('Canada','Germany','France');  --IN연산자 사용하기 


SELECT
 LastName,FirstName,Country
FROM
 customers
WHERE 
 Country NOT IN ('Canada','Germany','France');


SELECT
 LastName,FirstName
FROM
 customers
WHERE                   -- % : 0개이상의 문자열과 일치하는지 확인
 LastName LIKE '%son';  --lastname 이 son으로 끝나는것 출력

SELECT
 LastName,FirstName
FROM
 customers
WHERE                  -- _: 단일문자와 일치하는지 확인 
 FirstName LIKE '___a'; --4자리면서 a로끝나는 것 출력


SELECT
 TrackId,Name,Bytes
FROM
 tracks
ORDER BY
 Bytes DESC
LIMIT 7;   -- Bytes기준으로 내림차순으로 7개만 조회


SELECT
 TrackId,Name,Bytes
FROM
 tracks
ORDER BY
 Bytes DESC
LIMIT 4 OFFSET 3; --내림차순으로 4번째부터 7번째데이터만 조회

-- 04. Grouping data

SELECT
 Country
FROM
 customers
GROUP BY
 Country; --DISTICT에 ORDER BY 한 결과와 동일
          --GROUP BY는 더 특별한 기능있음


SELECT
 Country, COUNT(*)
FROM
 customers
GROUP BY
 Country; -- 카운트가 각그룹에 대한 집계된 값을 계산

SELECT
 Composer
FROM
 tracks
GROUP BY
 Composer; --중복없이 오름차순으로 작곡가필드 출력

SELECT
 Composer,AVG(Bytes)
FROM
 tracks
GROUP BY
 Composer
ORDER BY
 AVG(Bytes) DESC;

SELECT
 Composer,AVG(Milliseconds/60000) AS avgOfMinute
FROM
 tracks
WHERE
 avgOfMinute < 10
GROUP BY
 Composer;  --에러 발생 

 
-- 아래처럼하기
SELECT
 Composer,
 AVG(Milliseconds/60000) AS avgOfMinute
FROM
 tracks
GROUP BY
 Composer
HAVING
 avgOfMinute < 10;




-- 에러


-- 에러 해결
