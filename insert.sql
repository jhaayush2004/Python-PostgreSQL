INSERT INTO customers 
(first_name, last_name, email_address, phone_number, number_of_complaints)
VALUES
('John', 'Doe', 'jdoe@email.com', '5467876', 2),
('Vladimir', 'Putin', 'putin@email.com', '62466894', 0);

INSERT INTO customers
(first_name, last_name, email_address, phone_number, number_of_complaints)
VALUES
('Isabella', 'Rodriguez-Gonzales', 'isabella.rodriguez.gonzales.long.email.address@verylongdomainname.com', 777123456, 1);

INSERT INTO customers
(first_name, last_name, email_address, phone_number, number_of_complaints)
VALUES
('Liam', 'Chen', NULL, 123456789, 2);

INSERT INTO customers
(first_name, last_name, email_address, phone_number, number_of_complaints)
VALUES
('Noah', 'Wong', 'noah.wong@org.net', 303030303, NULL), -- NULL complaints
('Emma', 'Davis', NULL, 404040404, 1),             -- NULL email
('William', 'Garcia', 'billg@corp.com', 505050505, 0);  -- Zero complaints, all fields