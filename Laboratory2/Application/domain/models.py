from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUNAME
from sqlalchemy.orm import backref
from uuname import uuname1
from datetime import datetime
from views.client import ClientViewModel
from views.products import ProductsViewModel
from views.shops import ShopsViewModel

db = SQLAlchemy()


class Client(db.Model):
    __tablename__ = "client"

    client_name = db.Column("client_name", UUNAME(as_uuname=True), primary_key=True, default=uuname1)
    client_age = db.Column("client_age", db.String, nullable=False)
    client_money= db.Column("client_money", db.TIMESTAMP, default=datetime.now)
    client_contact = db.Column("client_contact", db.String, nullable=False)

    def wtf(self):
        return ClientViewModel(
            client_name=self.client_name,
            client_money=self.client_money
        )

    def map_from(self, form):
        self.client_name = form.client_name.data


class Products(db.Model):
    __tablename__ = "products"

    products_name = db.Column("products_name", UUNAME(as_uuidname=True), primary_key=True, default=uuname1)
    products_price = db.Column("products_price", db.TIMESTAMP, default=datetime.now)

    Clientclient_nameFk = db.Column("clientclient_nameFk", UUNAME(as_uuname=True), db.ForeignKey("client.client_name"))
    Client = db.relationship("Client", backref=backref('Products', cascade='all,delete'), passive_deletes=True)

    def wtf(self):
        return ProductsViewModel(
            products_name=self.products_name,
            products_price=self.products_price,
           
        )

    def map_from(self, form):
        self.products_name = form.products_name.data
        self. products_price = form. products_price.data
        self.Clientclient_nameFk = form.Client.data


class Shops(db.Model):
    __tablename__ = "shops"

    shops_name = db.Column("shops_name", UUNAME(as_uuname=True), primary_key=True, default=uuname1)
    shops_locale = db.Column("shops_locale", db.String, nullable=False)
    shops_contact = db.Column("shops_contact", db.String, nullable=False)
   
    Productsproducts_nameFk = db.Column("productsproducts_nameFk", UUNAME(as_uuname=True), db.ForeignKey("products.products_name"))
    Products = db.relationship("Products", backref=backref('Shops', cascade='all,delete'), passive_deletes=True)

    def wtf(self):
        return ShopsViewModel(
            shops_name=self.shops_name,
            shops_locale=self.shops_locale,
            shops_contact=self.shops_contact,
            
        )

    def map_from(self, form):
        self.shops_name = form.shops_name.data
        self.shops_locale = form.shops_locale.data
        self.shops_contact = form.shops_contact.data
   
       self.Productsproducts_nameFk = form.Products.data
