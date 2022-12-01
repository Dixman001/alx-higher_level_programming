-- create a table called first_table in the current database
-- If the table first_table already exists, your script should not fail
-- first_table description: id INT; name VARCHAR(256)

CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(1, "John", 10), 
(2, "Alex", 3), (3, "BOb", 14), (4, "George", 8);
