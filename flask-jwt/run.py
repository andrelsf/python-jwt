from os import environ
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

"""
    Parameters for SQLAlchemy
"""
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL_DEV')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

"""
    Adding JWT feature
"""
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
jwt = JWTManager(app)

"""
    Support of token blacklisting
"""
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_ALGORITHM'] = 'HS256'
app.config['JWT_CSRF_METHODS'] = ['POST', 'PUT', 'PATCH', 'DELETE']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)

import views, models, resources

"""
    Registry resources
"""
api.add_resource( resources.UserRegistry,        '/oauth/registry')
api.add_resource( resources.UserLogin,           '/oauth/login')
api.add_resource( resources.UserLogoutAccess,    '/oauth/logout/access')
api.add_resource( resources.UserLogoutRefresh,   '/oauth/logout/refresh')
api.add_resource( resources.TokenRefresh,        '/oauth/token/refresh')
api.add_resource( resources.AllUsers,            '/users')
api.add_resource( resources.SecretResource,      '/secret')