from db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# @login_manager.usuario_loader
# def get_user(usuario_id):
#     return usuario.query.filter_by(id=usuario_id).first()


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    login = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    dataCadastro = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __init__(self, nome, email, login, senha):
        self.nome = nome
        self.email = email
        self.login = login
        self.senha = generate_password_hash(senha)

    def verificarsenha(self, senha):
        return check_password_hash(self.senha, senha)

    @staticmethod
    def verificar_credenciais(login, senha):
        # Lógica para verificar as credenciais do usuário
        # Esta é apenas uma implementação simplificada, você deve adaptá-la às suas necessidades
        usuario = Usuario.query.filter_by(login=login).first()

        if usuario and usuario.verificarsenha(senha):
            return usuario
        else:
            return None
