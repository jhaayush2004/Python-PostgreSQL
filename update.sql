UPDATE customer
SET first_name = 'Ayush'
WHERE customer_id = 1

'we should put column name in double quotes and value in single quotes like
UPDATE TABLE_NAME 
SET “Column_name1” = ‘value1’, “Column_name2” = ‘value2’
 WHERE “ID” = ‘value’
'

DELETE FROM customer
WHERE customer_id = 3

'The DROP TABLE command deletes a table in the database
 • Syntax'
 DROP TABLE table_name;
 
'The TRUNCATE TABLE command deletes the data inside a table, but 
not the table itself
 • Syntax'
 TRUNCATE TABLE table_name