from flask import Blueprint, render_template, redirect,request,session,url_for,flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import User,db,Benefit
from middlewares.loggedin import loginrequired
import os, datetime


accounts = Blueprint("accounts", __name__)

@accounts.route('/account', methods=['GET','POST'])
@loginrequired
def account():
    if request.method=='POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']
        phone= request.form['phone']
        image = request.files['image']
        whatsapp = request.form['whatsapp']
        ext =  str(image.content_type)
        upload_dir = os.path.join(os.path.join(os.getcwd(), os.path.join('static','images')),str(image.filename).strip(''))
        if ext == 'image/png' or  ext== 'image/jpg' or ext == 'image/jpeg':
            image.save(upload_dir)
        else:
           pass
        user = User(username=username,password=password,phone=phone,whatsapp=whatsapp,email=email,thumb=str(image.filename))
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('accounts.account'))
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
                    session['role'] = 'user'
                    return redirect(url_for('accounts.dashboard'))
                else:
                    return "Password doesnt match"
            else:
                return "username not found"
        else:
            return " please fill the fields"

@accounts.route('/dashboard', methods=['GET'])
def dashboard():
    try:
        if session['id']:
            benefits = Benefit.query.filter_by(user_id=session['id']).all()
            user = User.query.filter_by(id=session['id']).first()
            if user:
                return render_template('account/dashboard.html', user=user, benefits=benefits)
    except KeyError:
        return redirect(url_for('accounts.account'))

@accounts.route("/logout", methods=['GET'])
def logout():
    user = User.query.get(session['id'])
    user.last_seen = datetime.datetime.utcnow()
    db.session.commit()
    session.pop('id')
    session.pop('username')
    return redirect('/')