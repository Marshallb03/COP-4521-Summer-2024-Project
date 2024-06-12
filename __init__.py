from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/college'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    from .models import User
    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(models, url_prefix='/')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    return app

def create_db(app):
    db.create_all(app=app)
    print('Database created.')
