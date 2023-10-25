CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name varchar(50) NOT NULL
);
CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  userID INTEGER NOT NULL,
  FOREIGN KEY(userId)
    REFERENCES users(id)
);

Insert into users(name)
VALUES
  ('하석주'),
  ('송윤미'),
  ('유하선');
Insert into articles(title, content, userId)
VALUES
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

SELECT * FROM articles
INNER JOIN users
  ON articles.userId = users.id;

SELECT articles.id, title, name FROM articles
INNER JOIN users
  ON articles.userId = users.id
WHERE users.id = 1;



SELECT * FROM articles
LEFT JOIN users
  ON articles.userId = users.id;

SELECT * FROM users
LEFT JOIN articles
  ON articles.userId = users.id;
