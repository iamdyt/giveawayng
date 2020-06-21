from flask import Blueprint, render_template
from models.models import Category,Benefit

indexB = Blueprint("index", __name__)

@indexB.route('/')
@indexB.route('/home')
@indexB.route('/index.php')
def index():
    categories = Category.query.all()
    benefits = Benefit.query.all()
    return render_template('index/home.html', categories=categories, benefits=benefits)
    