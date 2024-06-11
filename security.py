# security.py
from flask_login import login_required, current_user


def proteger_rotas(app):
    if current_user.is_authenticated:

        # Rotas que precisam de autenticação
        rotas_protegidas = ['/clientes', '/usuarios', '/ordensservico']

        for rota in rotas_protegidas:
            blueprint = obter_blueprint_por_prefixo(app, rota)
            if blueprint:
                rota_blueprint = rota.replace(blueprint.url_prefix, '')
                app.route(rota)(login_required(
                    blueprint.view_functions[rota_blueprint]))
    else:
        return redirect(url_for('login'))


def obter_blueprint_por_prefixo(app, prefixo):
    for blueprint_name, blueprint in app.blueprints.items():
        if blueprint.url_prefix == prefixo:
            return blueprint
    return None
