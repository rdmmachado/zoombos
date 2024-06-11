from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, Blueprint, session
from models.usuario import Usuario
from db import db

# Rota para listar clientes
login_blueprint = Blueprint('login', __name__)


@login_blueprint.route('/acesso_login', methods=['GET', 'POST'])
def acesso_login():

    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']

        # Usuario.query.filter_by(login=login).first()
        usuario = Usuario.query.filter_by(login=login).first()

        # if login and senha:
        if login and senha:
            # Verificar se as credenciais do usuário são válidas

            usuario = Usuario.verificar_credenciais(login, senha)

            if usuario:
                # Credenciais válidas, autenticar usuário
                session['usuario_id'] = usuario.id
                session['usuario_logado'] = True
                # Redirecionar para a página protegida após o login
                return redirect(url_for('index'))
            else:
                # Credenciais inválidas, exibir mensagem de erro
                ("Nao para a página principal...")
                mensagem = 'Credenciais inválidas. Por favor, tente novamente.'
                return redirect(url_for('login'))
                # return render_template('login.html', mensagem=mensagem)

    # Se o método for GET, exibir a página de login


@login_blueprint.route('/logout')
def logout():   # Limpar a sessão de usuário para fazer logout
    session.pop('usuario_logado', None)
    session.pop('usuario_id', None)  # Remover também o ID do usuário
    return redirect(url_for('login'))  # Redirecionar para a página de login
    # Limpar a sessão de usuário para fazer logout
    # session.pop('usuario_logado', None)
    # redirect(url_for('login'))
    # return render_template('login.html')
