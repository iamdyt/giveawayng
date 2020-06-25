from flask import Blueprint, render_template,session,redirect,url_for,request,flash
from models.models import Admin,db, Benefit, State, Category
from werkzeug.security import generate_password_hash,check_password_hash
from middlewares.protectadmin import is_admin

''' Note and Take care of these in all your blueprint route
    All routes with id are yet to be protected '''

admin = Blueprint('admin',__name__)

@admin.route('/account', methods=['GET'])
def getaccount():
    return render_template('admin/account.html')

@admin.route('/create', methods=['POST'])
def post_register():
    username = request.form['username']
    password = generate_password_hash(request.form['password'])
    phone = request.form['phone']
    email = request.form['email']
    admin = Admin(username=username,password=password,phone=phone,email=email)
    db.session.add(admin)
    db.session.commit()
    flash('Registration Successful,please login Now')
    return redirect(url_for('admin.getaccount'))

@admin.route('/login', methods=['POST'])
def post_login():
    username = request.form['lusername']
    password = request.form['lpassword']
    user = Admin.query.filter_by(username=username).first()
    if user:
        ispassword = check_password_hash(user.password,password)
        if ispassword is True:
            session['id'] = user.id
            session['user'] = user.username
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Username or Password incorrect')
            return redirect(url_for('admin.getaccount'))
    else:
        flash('User cannot be found')
        return redirect(url_for('admin.getaccount'))

@admin.route('/dashboard', methods=['GET'])
@is_admin
def dashboard():
    benefits = Benefit.query.all()
    return render_template('admin/dashboard.html', benefits=benefits)

@admin.route('/logout', methods=['GET'])
def logout():
    session.pop('id')
    session.pop('user')
    return redirect(url_for('admin.getaccount'))

# Item-Benefits

@admin.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    if request.method == 'GET':
        benefits = Benefit.query.get(id)
        states = State.query.all()
        cat = Category.query.all()
        return render_template('admin/edit.html', benefits=benefits, states=states, categories=cat)
    else:
      title = request.form['title']
      category = request.form['category']
      state = request.form['state']
      description = request.form['description']
      benefits = Benefit.query.get(id)
      benefits.title=title
      benefits.cat_id = category
      benefits.state_id=state
      benefits.desc=description
      db.session.commit()
    return redirect(url_for('admin.dashboard'))

@admin.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    if session:
        bene = Benefit.query.get(id)
        db.session.delete(bene)
        db.session.commit()
        return redirect(url_for('admin.dashboard'))
    else:
        return redirect(url_for('admin.getaccount'))

@admin.route('/moderate', methods=['POST'])
@is_admin
def moderate():
    item_id = request.form['id']
    status = request.form['status']
    item = Benefit.query.filter_by(id=item_id).first()
    item.moderation = status
    db.session.commit()
    return redirect(url_for('admin.dashboard'))

# States
@admin.route('/states', methods=['GET'])
@is_admin
def get_state():
    states =  State.query.all()
    return render_template('admin/states.html', states=states)


@admin.route('/post-state', methods=['POST'])
@is_admin
def post_state():
    state =  request.form['state']
    states =  State(name=state)
    db.session.add(states)
    db.session.commit()
    return redirect(url_for('admin.get_state'))

@admin.route('/remove-state/<int:id>', methods=['GET'])
def remove_state(id):
    state = State.query.filter_by(id=id).first()
    db.session.delete(state)
    db.session.commit()
    return redirect(url_for('admin.get_state'))

# Categories

@admin.route('/categories', methods=['GET'])
@is_admin
def get_cats():
    cats =  Category.query.all()
    return render_template('admin/categories.html', cats=cats)


@admin.route('/post-cat', methods=['POST'])
@is_admin
def post_cat():
    cat =  request.form['cat']
    icon =  request.form['icon']
    cat =  Category(name=cat, icon=icon)
    db.session.add(cat)
    db.session.commit()
    return redirect(url_for('admin.get_cats'))

@admin.route('/remove-cat/<int:id>', methods=['GET'])
@is_admin
def remove_cat(id):
    cat = Category.query.filter_by(id=id).first()
    db.session.delete(cat)
    db.session.commit()
    return redirect(url_for('admin.get_cats'))

    