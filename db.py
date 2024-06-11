from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://syszoomb3:Rdm!(03!(()!@xmysql.syszoomb.com.br/syszoomb3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
