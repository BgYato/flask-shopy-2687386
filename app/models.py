from app import db #Se llama al app a que dentro de ese módlo está el archivo init.py
from datetime import datetime

# Entidades del proyecto
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