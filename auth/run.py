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

"""
    Using the expired_token_loader decorator
    will now call this function whenever an expired
    but otherwise valid access token attemps to access an endpoint
"""
@jwt.expired_token_loader
def expiredTokenCallback(expired_token):
    token_type = expired_token['type']
    return {
        'status': 401,
        'message': '{} token has expired'.format(token_type)
    }, 401


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)

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