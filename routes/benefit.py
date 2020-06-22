from flask import Blueprint,request,session
from models.models import Benefit,Category,State,db
from flask import redirect, render_template, url_for
from middlewares.loggedin import signinrequired
import os

benefits = Blueprint('benefits', __name__)

@benefits.route('/create',methods=['GET'])
@signinrequired
def get_create():
    categories = Category.query.all()
    states = State.query.all()
    return render_template('account/new.html', categories=categories,states=states)

@benefits.route('/create', methods=['POST'])
@signinrequired
def post_create():
    title = request.form['title']
    category = request.form['category']
    state = request.form['state']
    imageone =  request.files['imageone']
    imagetwo = request.files['imagetwo']
    imagethree =request.files['imagethree']
    description = request.form['description']
    extone =  str(imageone.content_type)
    exttwo =  str(imagetwo.content_type)
    extthree =  str(imagethree.content_type)
    upload_dirone= os.path.join(os.path.join(os.getcwd(), os.path.join('static','images')), str(imageone.filename))
    upload_dirtwo= os.path.join(os.path.join(os.getcwd(), os.path.join('static','images')), str(imagetwo.filename))
    upload_dirthree= os.path.join(os.path.join(os.getcwd(), os.path.join('static','images')), str(imagethree.filename))
    if (extone == 'image/png' or  extone == 'image/jpg' or extone == 'image/jpeg') and (exttwo == 'image/png' or  exttwo == 'image/jpg' or exttwo == 'image/jpeg') and (extthree == 'image/png' or  extthree == 'image/jpg' or extthree == 'image/jpeg') :
        imageone.save(upload_dirone)
        imagetwo.save(upload_dirtwo)
        imagethree.save(upload_dirthree)
    else:
        pass
    benefit = Benefit(title=title,user_id=session['id'],cat_id=category,state_id=state,desc=description,thumbone=str(imageone.filename),thumbtwo=str(imagetwo.filename),thumbthree=str(imagethree.filename))
    db.session.add(benefit)
    db.session.commit()
    return redirect(url_for('accounts.dashboard'))

@benefits.route('/edit/<int:id>', methods=['GET','POST'])
# @signinrequired please take a look later
def edit(id):
    if request.method == 'GET':
        benefits = Benefit.query.get(id)
        states = State.query.all()
        cat = Category.query.all()
        return render_template('account/edit.html', benefits=benefits, states=states, categories=cat)
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
    return redirect(url_for('accounts.dashboard'))


@benefits.route('/single/<string:slug>', methods=['GET'])
def single(slug):
    single_item = Benefit.query.filter_by(slug=slug).first()
    cat = Category.query.all()
    return render_template('benefits/single.html', item=single_item, categories=cat )

@benefits.route('/delete/<int:id>', methods=['GET'])

def delete(id):
    if session:
        bene = Benefit.query.get(id)
        db.session.delete(bene)
        db.session.commit()
        return redirect(url_for('accounts.dashboard'))
    else:
        return redirect(url_for('accounts.account'))