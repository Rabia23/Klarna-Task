-- create databases
CREATE DATABASE IF NOT EXISTS klarnadb;
CREATE DATABASE IF NOT EXISTS test_klarnadb;

-- create user
CREATE USER 'klarna'@'%' IDENTIFIED WITH mysql_native_password BY 'klarna';

-- grant priviliges
GRANT ALL ON klarnadb.* TO 'klarna'@'%';
GRANT ALL ON test_klarnadb.* TO 'klarna'@'%';
FLUSH PRIVILEGES;
