CREATE TABLE contacts(
  pk INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  age INTEGER NOT NULL
);

PRAGMA table_info('contacts');

-- PK는 없어도 알아서 생성
CREATE TABLE contacts(
  email TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  age INTEGER NOT NULL
);

INSERT INTO contacts(email, name, age)
values('ssafy@ssafy.com', 'ssafy', 17);

INSERT INTO contacts(email, name, age)
values('ssafy@ssafy.com', 'ssafy', 17);

select * from contacts;
