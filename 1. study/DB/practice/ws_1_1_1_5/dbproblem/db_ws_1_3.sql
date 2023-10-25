SELECT first_name, country
FROM users
WHERE first_name = '건우' and country='경기도';

SELECT first_name, country, age
FROM users
WHERE country NOT IN ('경기도', '강원도') AND
  age BETWEEN 20 and 30
ORDER BY age;