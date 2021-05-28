from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://08ezYU3bp0:owSllN0RD4@remotemysql.com/08ezYU3bp0'
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)
db = SQLAlchemy(app)