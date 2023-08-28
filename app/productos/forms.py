from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class NewProductForm(FlaskForm):
    nombre = StringField("Nombre")
    precio = IntegerField("Precio")
    submit = SubmitField("Guardar")