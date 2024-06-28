from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import db, College  # This line now imports the db instance.
# from .load import load_data
import pandas as pd


# Remove db = SQLAlchemy() as it's now imported from models

#login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db:3306/college'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db with the app instance
    db.init_app(app)
    #login_manager.init_app(app)
    #login_manager.login_view = 'login'

    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    #@login_manager.user_loader
    #def load_user(user_id):
        #return User.query.get(int(user_id))

    return app

def create_db(app):
    with app.app_context():
        db.create_all()
        # load_data() 
        print('Database created.')