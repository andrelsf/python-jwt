from os import environ
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)

app.config.from_pyfile('./utils/config.py')

"""
    Flask CORS
"""
CORS(
    app, 
    resources={ r"/*": { "origins": "*" } },  
    methods=["GET", "POST", "PUT"],
    allow_headers=["Content-Type"]
)

"""
    Flask-RESTful
"""
api = Api(app)
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

"""
    Adding JWT feature
"""
jwt = JWTManager(app)

import auth.jwt
from errors.handler import handleException
import views, models, resources

"""
    Registry resources
"""
api.add_resource( resources.UserRegistry,        '/auth/registry')
api.add_resource( resources.UserVerify,          '/auth/verify')
api.add_resource( resources.UserLogin,           '/auth/login')
api.add_resource( resources.UserLogoutAccess,    '/auth/logout')
api.add_resource( resources.AllUsers,            '/users')                  # GET
api.add_resource( resources.SingleUser,          '/users/<int:user_id>')    # GET
api.add_resource( resources.UpdateStatusUser,    '/users/<int:user_id>')    # PUT
api.add_resource( resources.SecretResource,      '/secret')