# stores standard routes for website
from flask import Flask, Blueprint, render_template, request
import pandas as pd


views = Blueprint('views', __name__)


# LINK TO HOME PAGE - ABOUT
@views.route('/', methods=['GET'])
def about():
    return render_template("acerca-de.html")

# LINK TO DASHBOARD
@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")



# LINK TO NOTAS
@views.route('/notas', methods=['GET', 'POST'])
def notas():
    render_template("notas.html")

# LINK TO NOTAS_DETALLE
@views.route('/notas_detalle', methods=['GET', 'POST'])
def notas_detalle():
    return render_template("notas_detalle.html")



# LINK TO MENSAJES
@views.route('/mensajes', methods=['GET', 'POST'])
def mensajes():
    return render_template("mensajes.html")



# LINK TO CUENTA
@views.route('/cuenta', methods=['GET', 'POST'])
def cuenta():
    return render_template("cuentas.html")

# LINK TO CUENTA_FACTURAS
@views.route('/cuenta_facturas', methods=['GET', 'POST'])
def cuenta_facturas():
    return render_template("cuenta_facturas.html")
