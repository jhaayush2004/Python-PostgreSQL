ALTER TABLE customers
ADD COLUMN gender varchar(10) NULL ;

ALTER TABLE customers
ALTER COLUMN gender char(10) NULL;

ALTER TABLE customers
DROP COLUMN gender ;

'After adding column gender, we are adding values into it'
UPDATE customer
SET gender = CASE
    WHEN customer_id = 1 THEN 'M'
    WHEN customer_id = 2 THEN 'M'
    WHEN customer_id = 3 THEN 'F'
    WHEN customer_id = 4 THEN 'M'
    WHEN customer_id = 5 THEN 'F'
    WHEN customer_id = 6 THEN 'M'
    WHEN customer_id = 7 THEN 'F'
    WHEN customer_id = 8 THEN 'M'
    WHEN customer_id = 9 THEN 'M'
    ELSE gender
END
WHERE customer_id IN (1, 2, 3, 4, 5, 6, 7, 8, 9)
'The CASE statement allows you to specify different values for gender based on different WHEN conditions.

ELSE gender is important: If a customer_id doesnt match any WHEN clause, its gender value will remain unchanged. If you omit ELSE gender and a row doesnt match a WHEN clause, its gender would be set to NULL, which you likely dont want.

The WHERE clause is optional but good practice. If you omit it, the CASE statement will be evaluated for every row in the customers table. If you include it, it limits which rows the UPDATE applies to, making it more efficient if you only want to affect a subset.'