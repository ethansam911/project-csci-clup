use dc2633; #temporarily using IBM from Hunter. You can use your own db to test for now

CREATE TABLE IF NOT EXISTS customers(
customerID INT AUTO_INCREMENT UNIQUE,
password varchar(32),
firstName varchar(64),
middleName varchar(64),
lastName varchar(64),
email varchar(32),
cellnumber varchar(12)
);

#Testing table above table
-- insert into customers (password, firstName, middleName, lastName, address, zipCode) VALUES ("1234", "David", "middle", "Chen", "12as" ,"11235");
-- select * from customers;


CREATE TABLE IF NOT EXISTS company(
companyID INT AUTO_INCREMENT UNIQUE,
companyName varchar(32)


);


CREATE TABLE IF NOT EXISTS zipcode(
zipCode varchar(5),
city varchar(32),
state varchar(32),
);


