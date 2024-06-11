# Ordem_servico.py

from flask import Flask, render_template, redirect, url_for, request, jsonify, flash, Blueprint, session, send_file
from models.OrdemServico import OrdemServico
from models.cliente import Cliente
from db import db
from sqlalchemy import join, desc
from verificar import verificar_login
from flask_login import current_user, login_required
from datetime import datetime
import os
import tempfile
import json


# Rota para listar clientes
ordem_servico_blueprint = Blueprint('ordem_servico', __name__)


@ordem_servico_blueprint.route('/ordem_servico')
@verificar_login
def Ordem_servico():
    # Realizar uma junção entre as tabelas ordem_servico e clientes
    # Ordem_servico = db.session.query(OrdemServico, Cliente).join(
    #     Cliente, OrdemServico.cliente_id == Cliente.id).all()
    page = request.args.get('page', 1, type=int)
    per_page = 6  # Defina o número de itens por página
    ordens_servico = db.session.query(OrdemServico, Cliente).join(
        Cliente, OrdemServico.cliente_id == Cliente.id).order_by(desc(OrdemServico.id)).paginate(page=page, per_page=per_page, error_out=False)

    return render_template('ordem_servico/ordem_servico.html', ordens_servico=ordens_servico)

# Popula comobobox


@ordem_servico_blueprint.route('/cad_ordem_servico')
@verificar_login
def pesquisar_cliente():
    pesquisar_clientes = Cliente.query.all()
    return render_template('ordem_servico/cad_ordem_servico.html', pesquisar_cliente=pesquisar_clientes)


@ordem_servico_blueprint.route('/cad_ordem_servico', methods=['GET', 'POST'])
@verificar_login
def cad_ordem_servico():
    try:
        if request.method == 'POST':

           # Obter os dados do formulário
            # Verificar se cliente id foi selecionado ou foi escolhida a opção "Outros"
            cliente_id = None
            cliente_outros = None
            responsavel_type = None

            cliente_id = request.form.get('cliente_id')

            if cliente_id.isdigit() and int(cliente_id) > 0:
                # Um cliente específico foi selecionado
                cliente_id = cliente_id
            else:
                # A opção "Outros" foi selecionada, então pegue o ID do cliente inserido manualmente
                cliente_id = 0
                cliente_outros = request.form.get('NomeCliente')

            usuario_id = None
            usuario_id = session.get('usuario_id')
            data_realizacao = request.form.get('dataRealizacao')
            responsavel_type = request.form.get('responsavel_type')
            assinatura_responsavel = request.form.get('responsavel')
            assinatura_jardineiro = request.form.get('assinturaJardineiro')
            observacao = request.form.get('observacao')
            data = datetime.now()
           # Verificar se os campos de checkbox foram marcados e atribuir True ou False conforme necessário
            limpeza = True if request.form.get(
                'limpeza') is not None else False
            poda_grama = True if request.form.get(
                'poda-grama') is not None else False
            poda_plantas = True if request.form.get(
                'poda-plantas') is not None else False
            outros = True if request.form.get(
                'outrosServ') is not None else False

            # Se 'outros' foi marcado, obter a descrição dos outros serviços
            outros_descricao = None
            if outros:
                outros_descricao = request.form.get('outrosServdescricao')

            # # Validar se pelo menos um tipo de serviço foi selecionado
            # if not (limpeza or poda_grama or poda_plantas or outros):
            #     return jsonify({'error': 'Pelo menos um tipo de serviço deve ser selecionado.'}), 400

            # Criar um novo objeto OrdemServico com os dados do formulário
            nova_ordem_servico = OrdemServico(
                cliente_id=cliente_id,
                usuario_id=usuario_id,
                cliente=cliente_outros,
                data_realizacao=data_realizacao,
                limpeza=limpeza,
                poda_plantas=poda_plantas,
                poda_grama=poda_grama,
                outros=outros,
                outros_descricao=outros_descricao,
                responsavel_type=responsavel_type,
                assinatura_responsavel=assinatura_responsavel,
                assinatura_jardineiro=assinatura_jardineiro,
                observacao=observacao,
                data=data
            )

            # Adicionar a nova ordem de serviço ao banco de dados
            db.session.add(nova_ordem_servico)
            db.session.commit()

            return redirect(url_for('ordem_servico.Ordem_servico'))
        else:
            return render_template('ordem_servico/cad_ordem_servico.html')

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@ordem_servico_blueprint.route('/editar_ordem_servico/<int:ordem_servico_id>', methods=['GET', 'POST'])
@verificar_login
def editar_ordem_servico(ordem_servico_id):
    try:
        # Encontrar a ordem de serviço pelo ID
        ordem_servico = OrdemServico.query.get(ordem_servico_id)

        if ordem_servico is None:
            return jsonify({'error': 'Ordem de serviço não encontrada'}), 404

        if request.method == 'POST':
            # Atualizar os campos da ordem de serviço com os dados do formulário
            ordem_servico.cliente_id = request.form.get('cliente_id')
            ordem_servico.cliente = request.form.get('cliente_nome')
            ordem_servico.data_realizacao = request.form.get('dataRealizacao')
            ordem_servico.responsavel_type = request.form.get(
                'responsavel_type')
            ordem_servico.assinatura_responsavel = request.form.get(
                'assinatura_responsavel')
            ordem_servico.assinatura_jardineiro = request.form.get(
                'assinatura_jardineiro')
            ordem_servico.observacao = request.form.get('observacao')
            ordem_servico.data = datetime.now()

            # Atualizar os campos de checkbox
            ordem_servico.limpeza = True if request.form.get(
                'limpeza') is not None else False
            ordem_servico.poda_plantas = True if request.form.get(
                'poda-plantas') is not None else False
            ordem_servico.poda_grama = True if request.form.get(
                'poda-grama') is not None else False
            ordem_servico.outros = True if request.form.get(
                'outrosServ') is not None else False

            # Atualizar a descrição dos outros serviços, se aplicável
            if ordem_servico.outros:
                ordem_servico.outros_descricao = request.form.get(
                    'outrosServdescricao')
            else:
                ordem_servico.outros_descricao = None

            # Salvar as alterações no banco de dados
            db.session.commit()

            return redirect(url_for('ordem_servico.pesquisar_os'))

        else:
            return render_template('ordem_servico/editar_ordem_servico.html', ordem_servico=ordem_servico)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@ordem_servico_blueprint.route('/pdf_ordem_servico/<int:ordem_servico_id>', methods=['GET'])
@verificar_login
def pdf_ordem_servico(ordem_servico_id):
    try:
        ordem_servico, cliente = db.session.query(OrdemServico, Cliente).join(
            Cliente, OrdemServico.cliente_id == Cliente.id).filter(OrdemServico.id == ordem_servico_id).first()

        if not ordem_servico:
            return jsonify({'error': 'Ordem de serviço não encontrada'}), 404

    # Renderiza o template HTML com os detalhes da ordem de serviço e do cliente
        return render_template('ordem_servico/consulta_ordem_servico.html', ordem_servico=ordem_servico, cliente=cliente)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
