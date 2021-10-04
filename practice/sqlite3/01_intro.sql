CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);
DROP TABLE classmates;
SELECT * FROM classmates;
INSERT INTO classmates VALUES (1, '홍길동', 30, '서울'); 

INSERT INTO classmates VALUES 
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이싸피', 26, '광주'),
('박삼성', 29, '구미'),
('최전자', 28, '부산');

-- id 값확인
SELECT rowid, * FROM classmates;

-- READ
-- limit
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;


-- DELETE
DELETE FROM classmates WHERE rowid=5;
-- autoincrement
-- SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 
-- 재사용하는 것 방지(장고 기본 설정)

-- UPDATE
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;

-- WHERE 활용

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT first_name FROM users WHERE age>=30;

-- aggregate
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users;
SELECT SUM(age) FROM users;
SELECT MIN(age) FROM users;
SELECT MAX(age) FROM users;

SELECT AVG(age) FROM users where age>=30;
SELECT MAX(balance), last_name FROM users;
SELECT AVG(balance) FROM users where age>=30;

-- DATA types
CREATE TABLE tableN(
id INTEGER,
name TEXT);

INSERT INTO tableN values(1, 'TEXT');
INSERT INTO tableN values('2', 10.1);
INSERT INTO tableN values('2', 10.);
INSERT INTO tableN values('2', 10);
INSERT INTO tableN values('2b', 'TEXT');

select id, typeof(id), name, typeof(name) FROM tableN;

-- LIKE
SELECT * FROM users where age LIKE '2_';

SELECT COUNT(*) FROM users where phone LIKE '02_%';

SELECT COUNT(*) FROM users where first_name LIKE '%준';

-- order-by
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;

-- group-by
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;


-- ALTER
CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);
INSERT INTO articles values('1번제목', '1번 내용');

ALTER TABLE articles RENAME TO news;
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;





INSERT INTO classmates (name, age, address)
VALUES( '홍길동', 20, 'seoul' );

INSERT INTO classmates VALUES('홍길동', 20, 'seoul');

--  이게 안됨
insert into classmates
values(address='seoul', age=20, '홍길동');

insert into classmates (address, age, name)
values ('seoul', 20, '홍길동')