# clientes.py

from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, Blueprint
from models.cliente import Cliente
from db import db
from verificar import verificar_login

# Rota para listar clientes
clientes_blueprint = Blueprint('clientes', __name__)


@clientes_blueprint.route('/clientes')
@verificar_login
def clientes():
    clientes = Cliente.query.all()
    return render_template('clientes/clientes.html', clientes=clientes)

# @app.route('/clientes')
# def clientes():
#     return render_template('clientes/clientes.html')


@clientes_blueprint.route('/pesquisar-cliente', methods=['GET'])
@verificar_login
def pesquisar_cliente():
    nome_cliente = request.args.get('nome_cliente')
    if nome_cliente:
        clientes = Cliente.query.filter(
            Cliente.nome.like(f'%{nome_cliente}%')).all()
        return render_template('clientes/clientes.html', clientes=clientes)
    else:

        # Se nenhum nome de cliente foi fornecido, redirecione de volta para a página de clientes
        return redirect(url_for('clientes.clientes'))


@clientes_blueprint.route('/cadastrocliente', methods=['GET', 'POST'])
@verificar_login
def cadastrocliente():
    try:
        if request.method == 'POST':
            # Obter os dados do formulário
            nome = request.form['nome']
            telefone = request.form['telefone']
            endereco = request.form['endereco']

            # Criar um novo objeto Cliente com os dados do formulário
            novo_cliente = Cliente(
                nome=nome, telefone=telefone, endereco=endereco)

            # Adicionar o novo cliente ao banco de dados
            db.session.add(novo_cliente)
            db.session.commit()
            return redirect(url_for('clientes.clientes'))
        else:
            return render_template('clientes/cadastrocliente.html')

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@clientes_blueprint.route('/editarclientes/<int:cliente_id>', methods=['GET', 'POST'])
@verificar_login
def editarclientes(cliente_id):
    try:
        cliente = Cliente.query.get(cliente_id)

        # return redirect(url_for('visualizar_cliente', cliente_id=cliente.id))
        if request.method == 'GET':
            return render_template('clientes/editarclientes.html', cliente=cliente)

        if request.method == 'POST':
            cliente.nome = request.form['nome']
            cliente.telefone = request.form['telefone']
            cliente.endereco = request.form['endereco']
            # Atualiza outros campos conforme necessário

            # Salva as alterações no banco de dados
            db.session.commit()

            # Exibe uma mensagem de sucesso antes de redirecionar o usuário
            flash('Cliente atualizado com sucesso!', 'success')
            # return jsonify({'message': 'Cliente atualizado com sucesso!'}), 200
            clientes = Cliente.query.all()
            return redirect(url_for('clientes.clientes'))

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@clientes_blueprint.route("/p_cliente", methods=['GET'])
def p_cliente():
    # Renderize o template da página de pesquisa de clientes
    return render_template('pesquisa.html')


# # @app.route('/editarclientes')
# # def editarclientes():
# #     return render_template('clientes/editarclientes.html')
