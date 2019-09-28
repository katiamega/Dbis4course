INSERT INTO "CLIENT"(client_name,client_age,client_money,client_contact) JSON' { "client_name":"Kate", "client_age":"22", "client_money":"500", "client_contact":"0664839851" };
INSERT INTO "CLIENT"(client_name,client_age,client_money,client_contact) JSON' { "client_name":"Oleh", "client_age":"35", "client_money":"1000", "client_contact":"0674839861" };
INSERT INTO "CLIENT"(client_name,client_age,client_money,client_contact) JSON' { "client_name":"Olehander", "client_age":"30", "client_money":"3000", "client_contact":"0684839851" };
SELECT JSON * FROM "CLIENT";

INSERT INTO "TEST-ONLINE"(test-online_colour,test-online_price,test-online_productor,test-online_event) JSON' { "test-online_colour":"white", "test-online_price":"200", "test-online_productor":"Ukraine", "test-online_event":"Happy Birthday" };
INSERT INTO "TEST-ONLINE"(test-online_colour,test-online_price,test-online_productor,test-online_event) JSON' { "test-online_colour":"black", "test-online_price":"2000", "test-online_productor":"China", "test-online_event":"Weeding" };
INSERT INTO "TEST-ONLINE"(test-online_colour,test-online_price,test-online_productor,test-online_event) JSON' { "test-online_colour":"green", "test-online_price":"5000", "test-online_productor":"America", "test-online_event":"Work-party" };
SELECT JSON * FROM "TEST-ONLINE" ;

INSERT INTO "PRODUCTS" (products_name, products_price) JSON' { "products_name":"clothes", "products_price": ["500", "600", "700"] };
INSERT INTO "PRODUCTS" (products_name, products_price) JSON' { "products_name":"decoration", "products_price": ["1000", "1500", "1600"] };
INSERT INTO "PRODUCTS" (products_name, products_price) JSON' { "products_name":"jewellery", "products_price": ["3000", "4000", "5000"] };
SELECT JSON * FROM "PRODUCTS";

INSERT INTO "SHOPS" (shops_name, shops_locale, shops_contact, products) JSON' { "shops_name":"Clothes.ua", "shops_locale":"Kyiv", "shops_contact":"123-45-67", "products":"clothes" };
INSERT INTO "SHOPS" (shops_name, shops_locale, shops_contact, products) JSON' { "shops_name":"Decoration.com", "shops_locale":"Lviv", "shops_contact":"133-44-67", "products":"decoration" };
INSERT INTO "SHOPS" (shops_name, shops_locale, shops_contact, products) JSON' { "shops_name":"Jewellery.org", "shops_locale":"irpin", "shops_contact":"046-84-67", "products":"jewellery" };
SELECT JSON * FROM "SHOPS";


UPDATE "CLIENT" SET client_name = 'Anna' WHERE client_money = '1000';
SELECT JSON * FROM "CLIENT";

UPDATE "SHOPS" SET shops_locale='Kyiv' WHERE shops_name='Decoration.com';
SELECT JSON * FROM "SHOPS";

UPDATE "PRODUCTS" SET products_price =['3000', '4000', '6000'] WHERE products_name ='jewellery';
SELECT JSON * FROM "PRODUCTS";


UPDATE "CLIENT" SET client_name = [] WHERE client_money = '1000';
DELETE client_name FROM "CLIENT" WHERE client_money = '500';
SELECT JSON * FROM "CLIENT";

UPDATE "SHOPS" SET shops_locale = [] WHERE shops_name = 'Decoration.com';
DELETE shops_locale FROM "SHOPS" WHERE shops_name = 'Clothes.ua'';
SELECT JSON * FROM "SHOPS"; 

UPDATE "PRODUCTS" SET products_price =[] where products_name ='jewellery';
DELETE products_price FROM "PRODUCTS" WHERE products_name = 'decoration'; 
SELECT JSON * FROM "PRODUCTS";






