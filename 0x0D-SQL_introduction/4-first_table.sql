-- create a table called first_table in the current database
-- If the table first_table already exists, your script should not fail
-- first_table description: id INT; name VARCHAR(256)

CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
