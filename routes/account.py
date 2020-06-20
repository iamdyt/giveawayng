from flask import Blueprint, render_template, redirect,request,session,url_for,flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import User,db
import json

accounts = Blueprint("accounts", __name__)

@accounts.route('/account', methods=['GET','POST'])
def account():
    if request.method=='POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']
        phone= request.form['phone']
        user = User(username=username,password=password,phone=phone,email=email)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('account/account.html')

@accounts.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        usern = request.form['lusername']
        passkey = request.form['lpassword']
        if usern and passkey:
            uservar = User.query.filter_by(username=usern).first()
            if uservar:
                checked = check_password_hash(uservar.password,passkey)
                if checked:
                    session['id'] = uservar.id
                    session['username'] = uservar.username
                    return redirect(url_for('accounts.dashboard'))
                else:
                    return "Password doesnt match"
            else:
                return "username not found"
        else:
            return " please fill the fields"

@accounts.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('account/dashboard.html')        
       
    