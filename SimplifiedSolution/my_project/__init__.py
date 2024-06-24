from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4521@localhost/college_finder'
app.config['SECRET_KEY'] = '\xf0\xbb\x7f\x8f\xfa\x17\xc3\xf1\xaa\xaf\xdf\x1e\xdb\xf4\xcd\x15\x9c\xa8\xf7\xd9\x13\xda\x1d\xc4'

db = SQLAlchemy(app)

from my_project.routes import *

