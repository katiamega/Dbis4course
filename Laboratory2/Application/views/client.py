from wtforms import StringField, DateTimeField, SubmitField, validators
from flask_wtf import FlaskForm
from domain import models


class ClientViewModel(FlaskForm):
    client_name = StringField("client_name", [validators.DataRequired("Client name necessary")])
    client_age = DateTimeField("client_age")
    client_money = DateTimeField("client_money")


    Submit = SubmitField("Save")

    def domain(self):
        return models.Client(
            client_name=selfclient_name.data,
            client_age=self.client_age.data
            client_money=self.client_money.data
        )
