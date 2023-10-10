--필드 추가
ALTER TABLE examples
ADD COLUMN Address INTEGER;

PRAGMA table_info('examples');

ALTER TABLE
  examples
RENAME COLUMN
  Address TO PostCode;

ALTER TABLE
  examples
DROP COLUMN
  PostCode;

PRAGMA table_info('new_examples1');

ALTER TABLE
  examples
RENAME TO new_examples;

DROP TABLE new_examples1;

CREATE TABLE articles(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(100) NOT NULL,
content VARCHAR(200) NOT NULL,
createdAt DATE NOT NULL
);

INSERT INTO 
  articles(title, content, createdAt)
VALUES
  ('title2', 'world1', '2000-01-01'),
  ('title3', 'world2', '2000-01-01'),
  ('title1', 'world3', '2000-01-01');


UPDATE articles
SET title = 'update title'
where id = 1;



UPDATE articles
SET
  title = 'update title',
  content = 'update content'
where id = 2;
  
DELETE FROM articles
where id = 1;
select * from articles;


DELETE FROM articles
where id in (
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);
select * from articles;
