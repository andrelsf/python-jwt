# encoding: utf-8
# file: auth/utils/config.py

from os import environ

"""
    Parameters for SQLAlchemy
"""
SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL_DEV')
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

"""
    Adding JWT feature
"""
JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')

"""
    Support of token blacklisting
"""
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access']
JWT_ALGORITHM = 'HS256'
JWT_CSRF_METHODS = ['POST', 'PUT', 'PATCH', 'DELETE']