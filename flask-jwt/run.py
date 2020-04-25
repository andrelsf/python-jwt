from os import environ
from flask import Flask, json
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

app = Flask(__name__)

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

"""
    Handler Errors 400 e 404
"""
@app.errorhandler(HTTPException)
def handleException(error):
    """
        Return JSON instead of HTML for HTTP errors.
    """
    response = error.get_response()
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description
    })
    response.content_type = "application/json"
    return response

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
api.add_resource( resources.UserRegistry,        '/auth/registry')
api.add_resource( resources.UserLogin,           '/auth/login')
api.add_resource( resources.UserLogoutAccess,    '/auth/logout')
api.add_resource( resources.AllUsers,            '/users')                  # GET
api.add_resource( resources.SingleUser,          '/users/<int:user_id>')    # GET
api.add_resource( resources.UpdateStatusUser,    '/users/<int:user_id>')    # PUT
api.add_resource( resources.SecretResource,      '/secret')