#importacion o dependencias del proyecto
from flask import Flask, render_template
from config import Config
from flask_migrate import Migrate
from datetime import datetime
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, EmailField, PasswordField, SubmitField

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)

#inicialiar el objeto sqlalchemy 
db = SQLAlchemy(app)
migrate = Migrate(app , db )

#crear el formulario de registro de clientes.
class RegistroClienteForm(FlaskForm):
    username = StringField("Nombre de usuario")
    email = EmailField("Correo electronico")
    password = PasswordField("Contraseña")
    submit = SubmitField("Enviar")


# entidades del proyecto
class Cliente(db.Model):
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True)

class Producto(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer,
                   primary_key = True)
    nombre = db.Column(db.String(120),
                       unique = True)
    precio = db.Column(db.Numeric(precision = 10,
                                  scale = 2))
    imagen = db.Column(db.String(120),
                      unique = True)
    
class Venta(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer,
                   primary_key = True)
    fecha = db.Column(db.DateTime, 
                      default = datetime.utcnow)
    cliente_id = db.Column(db.Integer,
                      db.ForeignKey('clientes.id'))
    
class Detalle(db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer,
                    primary_key = True)
    producto_id = db.Column(db.Integer,
                        db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer,
                        db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)

@app.route('/clientes/create',
           methods = ['GET', 'POST'])
def crear_cliente():
    #instanciar formulario
    form = RegistroClienteForm()
    if form.validate_on_submit():
        #crear el nuevo cliente
        c = Cliente(username = form.username.data, password = form.password.data, email = form.email.data)
        db.session.add(c)
        db.session.commit()
        return "Se ha registado al cliente"
    return render_template('registro.html',
                           form = form)

@app.route('/clientes',
           methods = ['GET'])
def listar():
    clientes = Cliente.query.all()
    return render_template('listar.html', 
                           clientes = clientes)