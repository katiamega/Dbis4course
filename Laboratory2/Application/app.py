from flask import Flask, request, render_template, redirect, url_for
from domain.models import db, Сlient, Products, Shops
from domain.credentials import *
from views.client import СlientViewModel
from views.products import ProductsViewModel
from views.shops import AttributeViewModel
from views.dashboard import DashboardViewModel
from services.visualization import client_distribution_pie, products_attributes_population_bar
from sqlalchemy import desc
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", f"postgresql://{username}:{password}@{host}:{port}/{database}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    return render_template("layout.html")


@app.route("/client")
def client():
    all_client = Client.query.order_by(desc(Client.CreatedOn)).all()
    return render_template("client/index.html", client=all_schemas)


@app.route("/client/new", methods=["GET", "POST"])
def new_client():
    form =ClientlientViewModel()

    if request.method == "POST":
        if not form.validate():
            return render_template("client/create.html", form=form)
        else:
            client = form.domain()
            db.session.add(client)
            db.session.commit()
            return redirect(url_for("client"))

    return render_template("client/create.html", form=form)


@app.route("/client/delete/<uuname>", methods=["POST"])
def delete_client(uuid):
    client = Client.query.filter(client.client_name == uuname).first()
    if client:
        db.session.delete(client)
        db.session.commit()

    return redirect(url_for("client"))


@app.route("/client/<uuname>", methods=["GET", "POST"])
def update_client(uuname):
    client = Client.query.filter(Client.client_name == uuname).first()
    form = sclient.wtf()

    if request.method == "POST":
        if not form.validate():
            return render_template("client/update.html", form=form)

        client.map_from(form)
        db.session.commit()
        return redirect(url_for("client"))

    return render_template("client/update.html", form=form)


@app.route("/products")
def products():
    all_products = Products.query.join(Client).order_by(desc(Products.products_price)).all()
    return render_template("products/index.html", products=all_products)


@app.route("/products/new", methods=["GET", "POST"])
def new_products():
    form = ProductsViewModel()
    form.Client.choices = [(str(client.client_name), client.client_money) for client in Client.query.all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("products/create.html", form=form)
        else:
            client = form.domain()
            db.session.add(client)
            db.session.commit()
            return redirect(url_for("products"))

    return render_template("products/create.html", form=form)


@app.route("/products/delete/<uuname>", methods=["POST"])
def delete_products(uuname):
    products = Products.query.filter(Products.products_name == uuname).first()
    if products:
        db.session.delete(products)
        db.session.commit()

    return redirect(url_for("products"))


@app.route("/products/<uuname>", methods=["GET", "POST"])
def update_products(uuname):
    products = Products.query.filter(Products.products_name == uuname).first()
    form = products.wtf()
    form.Client.choices = [(str(client.client_name), client.client_money) for client in Client.query.all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("products/update.html", form=form)
        products.map_from(form)
        db.session.commit()
        return redirect(url_for("products"))

    return render_template("products/update.html", form=form)


@app.route("/shops")
def shops():
    all_shops = Shops.query.join(Products).order_by(desc(Shops.shops_name)).all()
    return render_template("shops/index.html", shops=all_shops)


@app.route("/shops/new", methods=["GET", "POST"])
def new_shops():
    form = ShopsViewModel()
    form.Products.choices = [(str(products.products_name), f"{products.products_price} ({products.Client.client_money})") for products
                           in Products.query.join(Client, Products.Clientclient_nameFk == Client.client_name).all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("shops/create.html", form=form)
        else:
            client = form.domain()
            db.session.add(client)
            db.session.commit()
            return redirect(url_for("shops"))

    return render_template("shops/create.html", form=form)


@app.route("/shops/<uuname>", methods=["GET", "POST"])
def update_shops(uuname):
    shops = Shops.query.filter(Shops.shops_name == uuname).first()
    form = shops.wtf()
    form.Products.choices = [(str(products.products_name), f"{products.products_price} ({products.Client.client_money})") for products
                           in Products.query.join(Client, Products.Clientclient_nameFk == Client.client_name).all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("shops/update.html", form=form)
        shops.map_from(form)
        db.session.commit()
        return redirect(url_for("shops"))

    return render_template("shops/update.html", form=form)


@app.route("/shops/delete/<uuname>", methods=["POST"])
def delete_shops(uuname):
    shops = Shops.query.filter(Shops.shops_name == uuname).first()
    if shops:
        db.session.delete(shops)
        db.session.commit()

    return redirect(url_for("shops"))


@app.route("/dashboard")
def dashboard():
    all_client = db.session.query(Client.client_name, Client.client_money).all()
    distinct_products = db.session.query(Products.products_name).distinct().all()
    dashboardViewModel = DashboardViewModel()
    if len(all_client):
        dashboardViewModel.Client = [(str(client.client_name), client.client_money) for client in all_client]
        dashboardViewModel.Client_distribution_data = client_distribution_pie(all_client[0][0])

    if len(distinct_products):
        dashboardViewModel.Products = distinct_products
        dashboardViewModel.Products_shops_population_data = products_shops_population_bar(
            distinct_products[0][0])

    return render_template("dashboard/index.html", model=dashboardViewModel)


@app.route("/client_distribution/<uuname>")
def client_distribution(uuname):
    return client_distribution_pie(name)


@app.route("/products_shops_population/<name>")
def products_shops_population(name):
    return products_shops_population_bar(name)


if __name__ == "__main__":
    app.run()
