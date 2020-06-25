from functools import wraps
from flask import session, redirect,url_for


def is_admin(func):
    @wraps(func)
    def check():
        try:
            if session['role'] or not session:
                return redirect(url_for('accounts.account'))
            else:
                return func()
        except KeyError:
            return redirect(url_for('accounts.account'))
    return check
