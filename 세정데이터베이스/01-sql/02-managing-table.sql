-- id, title, content의 열을 가진 article 테이블 생성
-- PRIMARY KEY=(NOT NULL + UNIQUE)
-- PRIMARY KEY AUTOINCREMENT => 공식

CREATE TABLE article(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    userid INTEGER NOT NULL,
    FOREIGN KEY(userid) REFERENCES user(id)
);

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(30) NOT NULL UNIQUE,
    email varchar(100) UNIQUE
    
);

INSERT INTO user (username,email)
 VALUES 
    ('이순신','sunsin@email.com'),
    ('유관순','ugs@email.com');



-- 삭제는 : DROP
DROP TABLE article;



-- 데이터를 집어넣기 넣는방법 : INSERT
-- INSERT짝꿍은 INTO
INSERT INTO article(title,content,userid)
VALUES 
 ('제목2','USER1이쓴글',1) ;



--article테이블에 userid가 user테이블에 존재하지 않은경우에 삭제
DELETE 
 FROM article
WHERE userid not in(
 SELECT id FROM user
 );
 







--ALTER TABLE :테이블 및 컬럼 수정
-- 칼럼추가
ALTER TABLE article 
 ADD COLUMN created_at DATE NOT NULL DEFAULT '';

ALTER TABLE article
 RENAME COLUMN contents TO contentsss;

--칼럼삭제
ALTER TABLE article
DROP COLUMN created_at ;  -- 에러임...이유모름..





-- 기존의 레코드를 수정하기(UPDATE)
UPDATE article 
 SET created_at = DATE()
--기존의 비어있는 created_at에 모두 DATE추가해라
--특정 레코드만 선택하려면 WHERE절
WHERE id = 3;

UPDATE article
 SET title = 'updated title',
     content = 'new content',
     created_at = '2023-10-20'
WHERE id = 4;


-- DELETE 는 레코드하나를 삭제하는 것
DELETE 
 FROM article
WHERE title = '제목2';

SELECT * -- 위치에 DELETE 
 FROM article
 WHERE id IN (
 SELECT id
 FROM article
 ORDER BY id
 LIMIT 1 
 );-- 제일 오래됀 게시글의 id
 
 
 
 