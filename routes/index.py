from flask import Blueprint, render_template

indexB = Blueprint("index", __name__)

@indexB.route('/')
@indexB.route('/home')
@indexB.route('/index.php')
def index():
    return render_template('index/home.html')
    