INSERT INTO client  (client_name ,client_age,client_money, client_contact)
VALUES ('Kate', 20, 1000, '0673845599');

INSERT INTO client   (client_name ,client_age,client_money, client_contact)
VALUES ('Olexander', 15, 2500,'0685431120');

INSERT INTO client   (client_name ,client_age,client_money, client_contact)
VALUES ('Oleh', 40, 5000,'0981234566');


-- 
INSERT INTO products  (products_name, products_price)
VALUES ('decoration', 950);

INSERT INTO products  (products_name, products_price)
VALUES ( 'furniture', 2400);

INSERT INTO products (products_name, products_price)
VALUES ( 'clothes', 3200);


-- 
INSERT INTO shops (shops_name, shops_locale, shops_contact)
VALUES ('Present', 'Kyiv',  '345678387');

INSERT INTO shops  (shops_name, shops_locale, shops_contact)
VALUES ( 'House', 'Kyiv','555786112');

INSERT INTO shops (shops_name, shops_locale, shops_contact)
VALUES ( 'Clothes', 'Lviv','123456777');

-- 
INSERT INTO test-online (test-online_colour, test-online_productor, test-online_event, test-online_price)
VALUES ('black', 'Ukraine','Weeding', 1000);

INSERT INTO test-online(test-online_colour, test-online_productor, test-online_event, test-online_price)
VALUES ( 'white', 'China','Party', 2000);

INSERT INTO test-online (test-online_colour, test-online_productor, test-online_event, test-online_price)
VALUES ( 'yellow', 'America','Birthday',3000);

-- 
INSERT INTO Client pass test (client_name)
VALUES ('Kate');

INSERT INTO Client pass test (client_name)
VALUES ('Olexander');

INSERT INTO Client pass test (client_nam)
VALUES ('Oleh');
--

INSERT INTO List (products_name)
VALUES ('decoration');

INSERT INTO List (products_name)
VALUES ( 'furniture');

INSERT INTO List  (products_name)
VALUES ( 'clothhes');
---

INSERT INTO Pr in shops (shops_name, products_name)
VALUES ('Beauty', 'decoration');

INSERT INTO Pr in shops (shops_name, products_name)
VALUES ( 'House', 'furniture');

INSERT INTO Pr in shops  (shops_name, products_name)
VALUES ( 'Clothes', 'clothes');
----
INSERT INTO Client choose shops (client_name, shops_name)
VALUES ('Katy', 'Beauty');

INSERT INTOClient choose shops (client_name, shops_name)
VALUES ('Olexander', 'House');

INSERT INTO Client choose shops (client_name, shops_name)
VALUES ('Oleh', 'Clothes');
