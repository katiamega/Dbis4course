from wtforms import StringField, DateTimeField, SubmitField, BooleanField, SelectField, validators
from flask_wtf import FlaskForm
from domain import models
from uuname import UUNAME


class ProductsViewModel(FlaskForm):
    products_name = StringField("products_name", [validators.DataRequired("Products name necessary")])
    products_price = DateTimeField("products_price")
    Client = SelectField("Client", validators=[validators.DataRequired()])

    Submit = SubmitField("Save")

    def domain(self):
        return models.Products(
            products_name=self.products_name.data,
            products_price=self.products_price.data,
            Clientclient_nameFk=UUNAME(self.Client.data)
        )
