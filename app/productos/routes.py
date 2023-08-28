from app.productos import productos
from flask import render_template
from .forms import NewProductForm

@productos.route('/create')
def crear():
    form = NewProductForm()
    return render_template('new.html', form = form)

@productos.route('/read')
def leer():
    return 'aqui vamos a consultas productos'

@productos.route('/delete')
def eliminar():
    return 'aqui vamos a eliminar productos'

@productos.route('/update')
def actualizar():
    return 'aqui vamos a actualizar productos'