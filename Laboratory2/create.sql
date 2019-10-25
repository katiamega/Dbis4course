create table Сlient(
	client_name VARCHAR2(20) primary key,
	client_age DATE NOT NULL,
	client_money INTEGER NOT NULL,
	client_contact INTEGER NOT NULL,);
	
create table Test-online(
   test-online_colour VARCHAR2(10) NOT NULL,
	test-online_price INTEGER primary key,
	test-online_productor VARCHAR2(20) NOT NULL,
	test-online_event VARCHAR2(20) NOT NULL);

create table Clients pass tests(
	client_name VARCHAR2(20) NOT NULL references Сlient(client_name);
	
create table Products(
	products_name VARCHAR2(20) NOT NULL,
	products_price INTEGER primary key );

create table List(
	products_name VARCHAR2(20) NOT NULL references Products(products_name); 

create table Pr in shops(
	products_name VARCHAR2(20) NOT NULL references Products(products_name),
  shops_name  VARCHAR2(20) NOT NULL references Shops(shops_name)
	primary key (products_name,shops_name));

create table Shops(
	shops_name VARCHAR2(20) primary key,
	shops_locale VARCHAR2(20) NOT NULL,
	shops_contact INTEGER NOT NULL);

create table Client choose shop(
	shops_name VARCHAR2(20) NOT NULL references Shops(shops_name),
	client_name VARCHAR2(20)NOT NULL references Client(client_name)
	primary key (shops_name,client_name));

