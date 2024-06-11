# verificar.py

from functools import wraps
from flask import session, redirect, url_for


def verificar_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_logado' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
