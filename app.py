from flask_login import UserMixin
from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, session
from db import init_db, db
from flask_migrate import Migrate
from security import proteger_rotas
from flask_login import login_user, logout_user, LoginManager, login_required, UserMixin
from models.cliente import Cliente
from models.usuario import Usuario

from blueprints.clientes import clientes_blueprint
from blueprints.login import login_blueprint
from blueprints.usuarios import usuarios_blueprint
from blueprints.ordem_servico import ordem_servico_blueprint
from blueprints.firebase_store import firebase_store_blueprint

import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import storage
import base64
import re
import uuid


app = Flask(__name__)
app.static_folder = 'static'
app.config['DEBUG'] = True
app.secret_key = 'e782b397b44841218421947621422452942228412274212198219476'
login_manager = LoginManager(app)


# Inicializa o banco de dados com as configurações
init_db(app)

# Inicializa o banco de dados com as configurações
migrate = Migrate(app, db)

# Registrar blueprints

app.register_blueprint(clientes_blueprint, url_prefix='/clientes')
app.register_blueprint(usuarios_blueprint, url_prefix='/usarios')
app.register_blueprint(ordem_servico_blueprint, url_prefix='/ordem_servico')
app.register_blueprint(login_blueprint, url_prefix='/login')
# app.register_blueprint(firebase_store_blueprint, url_prefix='/firebase_store')


@login_manager.user_loader
def load_user(user_id):
    # Implemente a lógica para carregar o usuário com base no user_id
    # Substitua User pelo seu modelo de usuário
    return User.query.get(int(user_id))


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/')
def login():
    return render_template('login.html')


# @app.route('/popup')
# def popup():
#     return render_template('pesquisa.html')


if __name__ == '__main__':
    app.run(debug=True)
