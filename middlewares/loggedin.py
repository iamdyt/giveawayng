from flask import session,redirect,url_for
from functools import wraps

def loginrequired(func):
    @wraps(func)
    def isloggedin():
        if session:
            return redirect(url_for('accounts.dashboard'))
        else:
            return func()
    return isloggedin
