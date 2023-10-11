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