-- 01. Querying data
SELECT
  LastName
FROM
  employees;

SELECT
  LastName, FirstName
FROM
  employees;

SELECT
  *
FROM
  employees;

-- 실제로 테이블의 FirstName이 바뀐 것은 아님, 출력만 바뀐 것임
SELECT
  FirstName AS '이름'
FROM
  employees;

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;

-- 02. Sorting data
SELECT
  FirstName
FROM
  employees
ORDER BY
  -- ASC가 기본값이라서 안 써도 됨
  FirstName ASC;

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
  --먼저 정렬된 것이 우선시 되네
  Country DESC,
  City ASC;

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시
-- Null이 가장 작은값으로 취급됨
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;

-- 03. Filtering data
-- 중복없이
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;


-- City 가 'Prague'인 것 찾기(검색 조건)
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

-- City 가 'Prague'가 아닌것 찾기(검색 조건)
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

-- NULL은 약간 다름(IS NULL),
-- ~이고: AND 이용
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

-- ~이거나: OR 이용
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';

-- 범위 관련
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  -- 틀린방식(아래)
  -- 100000<=Bytes<=500000;
  -- 올바른 방식(아래)
  Bytes BETWEEN 100000 AND 500000;
  -- 올바른 방식(아래)
  -- Bytes >= 100000 
  -- AND Bytes <= 500000;

-- 정렬을 할 때(ORDER BY)는 WHERE보단 뒤에 와야됨
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

-- 결과는 맞지만 반복의 느낌..
SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada','Germany','France');

  -- Country = 'Canada'
  -- OR Country = 'Germany'
  -- OR Country = 'France';

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada','Germany','France');

-- son으로 끝나는 데이터 조회
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  -- %: 0개부터 여러개
  LastName LIKE '%son';

-- 필드 값이 4자리이면서 'a'로 끝
SELECT
  LastName, FirstName
FROM
  customers
WHERE
-- _: 오로지 하나
  FirstName LIKE '___a';

-- 출력제한(일부만 조회)
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4;
-- 보면 순서 반대죠?
-- LIMIT 4 OFFSET 3;

-- 04. Grouping data
-- Filtering data의 DISTINCT에 ORDER BY 한 것과 유사
-- 다만, Group BY는 좀 더 강력한 기능이 있음(집계함수)
SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

SELECT
-- 특이하게 AVG가 있네? 나머진 동일
  Composer, AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer DESC;

-- 그룹화의 집계항목에 대한 조건은 WHERE이 아닌 HAVING 이용
-- 집계항목이 아닌 것과 구분하기 위해서
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
