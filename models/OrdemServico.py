from db import db


class OrdemServico(db.Model):
    __tablename__ = 'ordem_servico'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey(
        'Clientes.id'), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        'usuarios.id'), nullable=False)
    cliente = db.Column(db.String(255), nullable=True)
    data_realizacao = db.Column(db.DateTime, nullable=False)
    limpeza = db.Column(db.Boolean, nullable=True, default=False)
    poda_plantas = db.Column(db.Boolean, nullable=True, default=False)
    poda_grama = db.Column(db.Boolean, nullable=True, default=False)
    outros = db.Column(db.Boolean, nullable=True, default=False)
    outros_descricao = db.Column(db.String(255), nullable=True)
    responsavel_type = db.Column(db.String(50), nullable=False)
    assinatura_jardineiro = db.Column(db.String(255), nullable=True)
    assinatura_responsavel = db.Column(db.String(255), nullable=True)
    observacao = db.Column(db.String(255), nullable=True)
    data = db.Column(db.DateTime, nullable=False)

    def __init__(self, cliente_id, usuario_id, cliente, data_realizacao, responsavel_type, assinatura_responsavel, assinatura_jardineiro, limpeza=False, poda_plantas=False, poda_grama=False, outros=False, outros_descricao=None, observacao=None, data=None):
        self.cliente_id = cliente_id
        self.usuario_id = usuario_id
        self.cliente = cliente
        self.data_realizacao = data_realizacao
        self.responsavel_type = responsavel_type
        self.assinatura_responsavel = assinatura_responsavel
        self.assinatura_jardineiro = assinatura_jardineiro
        self.limpeza = limpeza
        self.poda_plantas = poda_plantas
        self.poda_grama = poda_grama
        self.outros = outros
        self.outros_descricao = outros_descricao
        self.observacao = observacao
        self.data = data
