from wtforms import StringField, DateTimeField, SubmitField, BooleanField, SelectField, validators
from flask_wtf import FlaskForm
from domain import models
from uuname import UUNAME
from domain.layout import data_types


class ShopsViewModel(FlaskForm):
    shops_name = StringField("shops_name", [validators.DataRequired("Attribute name is required")])
    shops_locale = DateTimeField("shops_locale")
    shops_contact = DateTimeField("shops_contact")
    Products = SelectField("Products", validators=[validators.DataRequired()])

    Submit = SubmitField("Save")

    def domain(self):
        return models.Shops(
            shops_name=self.shops_name.data,
            shops_locale=self.shops_locale.data,
            shops_contact=self.shops_contact.data,
           
            Productsprodukts_nameFk=UUNAME(self.Products.data)
        )
