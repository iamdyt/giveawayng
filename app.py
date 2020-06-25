from flask import Flask
from routes.index import indexB
from models.models import db
from routes.account import accounts
from routes.benefit import benefits
from flask_moment import Moment
from routes.admin import admin





# Registering Package  Instance
app = Flask(__name__)
moment = Moment(app)
moment.init_app(app)

# @app.template_filter('humanize')
# def humanize(value):
#     return datetime.strftime(date(int(value)))

# Blueprint registering
app.register_blueprint(indexB)
app.register_blueprint(accounts, url_prefix='/user')
app.register_blueprint(benefits,url_prefix='/item')
app.register_blueprint(admin, url_prefix='/enter/administrator')

# Database Connection & Session
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@localhost/flasky"
app.config['SECRET_KEY'] = 'pbkdf2:sha256:150000$Ciwc'

# Connecting DB Model to app.py
db.init_app(app)

# with app.app_context():
#     db.drop_all()
# db.create_all(app=app)  

if __name__ == "__main__":
    
    app.run(debug=True)