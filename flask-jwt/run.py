from os import environ
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL_DEV')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

import views, models, resources

api.add_resource( resources.UserRegistry,        '/oauth/registry')
api.add_resource( resources.UserLogin,           '/oauth/login')
api.add_resource( resources.UserLogoutAccess,    '/oauth/logout/access')
api.add_resource( resources.UserLogoutRefresh,   '/oauth/logout/refresh')
api.add_resource( resources.TokenRefresh,        '/oauth/token/refresh')
api.add_resource( resources.AllUsers,            '/users')
api.add_resource( resources.SecretResource,      '/secret')