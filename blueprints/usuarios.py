from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, Blueprint, session
from models.usuario import Usuario
from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from verificar import verificar_login

# Rota para listar usuarios
usuarios_blueprint = Blueprint('usuarios', __name__)

# -------------------------parte de usuario


@usuarios_blueprint.route('/usuario')
@verificar_login
def usuario():
    usuarios = Usuario.query.all()
    return render_template('usuarios/usuario.html', usuarios=usuarios)


@usuarios_blueprint.route('/pesquisar_usuario', methods=['GET'])
@verificar_login
def pesquisar_usuario():
    nome = request.args.get('nome')
    if nome:
        usuario = Usuario.query.filter(Usuario.nome.like(f'%{nome}%')).all()
        return render_template('usuarios/usuario.html', usuarios=usuario)
    else:
        return redirect(url_for('usuarios.usuario'))

# Registar um novo usuario


@usuarios_blueprint.route('/cadastro_usuario', methods=['GET', 'POST'])
@verificar_login
def cadastro_usuario():
    try:
        if request.method == 'POST':
            # Obter os dados do formulário
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            # Criar um novo objeto Cliente com os dados do formulário
            usuario = Usuario(nome=nome, email=email, senha=senha)

            db.session.add(usuario)
            db.session.commit()

            return redirect(url_for('usuarios/pesquisar_usuario'))
        else:
            return render_template('usuarios/cadastrousuario.html')

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@usuarios_blueprint.route('/editar_usuario/<int:usuario_id>', methods=['GET', 'POST'])
@verificar_login
def editar_usuario(usuario_id):
    try:
        usuario = Usuario.query.get(usuario_id)
        # return redirect(url_for('visualizar_cliente', cliente_id=cliente.id))
        if request.method == 'GET':
            return render_template('usuarios/editarusuario.html', usuario=usuario)

        if request.method == 'POST':
            usuario.nome = request.form['nome']
            usuario.email = request.form['email']
            usuario.senha = generate_password_hash(request.form['senha'])
            # Salva as alterações no banco de dados
            db.session.commit()

            # Exibe uma mensagem de sucesso antes de redirecionar o usuário
            flash('Usuario atualizado com sucesso!', 'success')
            # return jsonify({'message': 'Cliente atualizado com sucesso!'}), 200
            return render_template('usuarios/usuario.html')

    except Exception as e:
        return jsonify({'error': str(e)}), 500
