from flask import session,redirect
def is_Logged_in(func):
    if session['username']:
        return redirect('accounts.dashboard')
    else:
        return func