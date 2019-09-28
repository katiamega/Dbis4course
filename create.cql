CREATE KEYSPACE keyspace_my
WITH replication = {
	'class' : 'SimpleStrategy',
	'replication_factor' : 1
};


CREATE TABLE keyspace_my."CLIENT" (
	client_name text,
	client_age int,
	client_money int-static,
	client_contact int,
	PRIMARY KEY (client_name, client_money)
);

CREATE TABLE keyspace_my."TEST-ONLINE" (
	test-online_colour text,
	test-online_price int,
	test-online_productor text,
	test-online_event text,
	PRIMARY KEY (test-online_price)
);

CREATE TABLE keyspace_my."PRODUCTS" (
	products_name text,
	products_price LIST<int>,
	PRIMARY KEY (products_name)
);


CREATE TABLE keyspace_my."SHOPS" (
	shops_name text,
	shops_locale text(40),
	shops_contact int,
	products map<products_price, text>,
        PRIMARY KEY (shops_name)
);


DROP TABLE IF EXISTS "CLIENT_TEST-ONLINE";
CREATE TABLE IF NOT EXISTS "CLIENT_TEST-ONLINE" (
client_name text,
client_age int,
client_money int-static,
client_contact int,
test-online_colour text,
test-online_price int,
test-online_productor text,
test-online_event text,
PRIMARY KEY ( (client_money), test-online_price)
);

SELECT test-online_price FROM TEST-ONLINE
  WHERE client_money '=';
  
DROP TABLE IF EXISTS "SHOPS_PRODUCTS";
CREATE TABLE IF NOT EXISTS "SHOPS_PRODUCTS" (
shops_name text,
shops_locale text(40),
shops_contact int,
products map<products_price, text>,
products_name text,
products_price LIST<int>,
PRIMARY KEY ( (shops_name), products_price)
);

SELECT shops_name FROM SHOPS
  WHERE products_price '=';
  
DROP TABLE IF EXISTS "CLIENT_PRODUCTS";
CREATE TABLE IF NOT EXISTS "CLIENT_PRODUCTS" (
client_name text,
client_age int,
client_money int-static,
client_contact int,
products map<products_price, text>,
products_name text,
products_price LIST<int>,
PRIMARY KEY ( (products_price), client_money)
);
  
SELECT products_price FROM PRODUCTS
  WHERE client_money '=';
 
DROP TABLE IF EXISTS "CLIENT_PRODUCTS";
CREATE TABLE IF NOT EXISTS "CLIENT_PRODUCTS" (
client_name text,
client_age int,
client_money int-static,
client_contact int,
products map<products_price, text>,
products_name text,
products_price LIST<int>,
PRIMARY KEY ( (products_name, products_price), client_money)
); 

SELECT products_name and products_price FROM PRODUCTS
  WHERE client_money '=';  



