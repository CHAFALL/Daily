
--create
CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

.mode csv
.import users.csv users
-- .mode COLUMN

--users 테이블에서 이름, 나이, 계좌잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌잔고가 많은 순으로 정렬해서 조회하시오

SELECT first_name, age, balance
FROM users
ORDER BY age, balance DESC
LIMIT 10;



-- db_ws_1_2.sql

SELECT first_name, age
FROM users
ORDER BY first_name, age DESC;

-- db_ws_1_3.sql
SELECT first_name, country
FROM users
WHERE first_name = '건우' and country='경기도';

SELECT first_name, country, age
FROM users
WHERE country NOT IN ('경기도', '강원도') AND
  age BETWEEN 20 and 30
ORDER BY age;

-- db_ws_1_4.sql
SELECT first_name, phone, country
FROM users
WHERE phone LIKE '%-51__-%' AND country != '서울';

-- db_ws_1_5.sql

SELECT * FROM users
ORDER BY age
LIMIT 40, 20;
-- LIMIT 20 OFFSET 40;