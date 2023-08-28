from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import mi_blueprint
from app.productos import productos
from flask_bootstrap import Bootstrap

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

#inicialiar el objeto sqlalchemy 
db = SQLAlchemy(app)
migrate = Migrate(app , db )

#registrar modulos
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

# Es importante importar los modelos al final del init para que no genere errores
from .models import Cliente, Venta, Producto, Detalle