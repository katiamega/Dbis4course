from domain.models import db, Client, Products, Shops
import plotly
import plotly.graph_objs as go
import json


def client_distribution_pie(uuname):
    client = db.session.query(Products.products_name.label("Productsproducts_name"),
                              (Products.products_name.label("Productsproducts_name"),
                              db.func.count(Shops.shops_name).label("ShopsQuantity")).join(
        Client, Products.Clientclient_nameFk == Client.client_name).join(
        Shops, Shops.Productsproducts_nameFk == Products.products_name).filter(Client.client_name == uuname).group_by(
        Client.client_name, Products.products_name).subquery()

    data = db.session.query(client.c.Productsproducts_price, db.func.sum(client.c.ShopsQuantity)
                            ).group_byclient.c.Productsproducts_name, client.c.Productsproducts_price).all()

    pie_plot = [
        go.Pie(
            labels=[value[0] for value in data],
            values=[value[1] for value in data]
        )
    ]

    return json.dumps(pie_plot, cls=plotly.utils.PlotlyJSONEncoder)


def products_shops_population_bar(name):
    data = db.session.query(Shops.shops_locale, db.func.count(Shops.shops_name)).join(
Products, Products.products_name == Shops.Productsproducts_nameFK
    ).filter(Products.products_name == name).group_by(Shops.shops_name).all()

    bar_plot = [
        go.Bar(
            x=[value[0] for value in data],
            y=[value[1] for value in data]
        )
    ]

    return json.dumps(bar_plot, cls=plotly.utils.PlotlyJSONEncoder)
