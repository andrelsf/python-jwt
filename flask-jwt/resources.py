from models import UserModel, RevokedTokenModel
from datetime import timedelta
from flask import request
from flask_restful import Resource, reqparse

from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)

class UserRegistry(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', help="This field cannot be blank", required=True)
        self.parser.add_argument('email', help="This field cannot be blank", required=True)
        self.parser.add_argument('password', help="This field connot be blank", required=True)

    def post(self):
        data = self.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {
                'message': 'User {} already exits'.format(data['email'])
            }

        new_user = UserModel(
            name = data['name'],
            email = data['email'],
            password = UserModel.generate_hash(data['password'])
        )
        try:
            new_user.save_to_db()
            return {
                'status': 'success',
                'message': 'User {} was created'.format(data['email'])
            }, 201
        except:
            return {
                'status': 'fail',
                'message': 'Something went wrong'
            }, 500

class UserLogin(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', help="This field cannot be blank", required=True)
        self.parser.add_argument('password', help="This field connot be blank", required=True)

    def post(self):
        data = self.parser.parse_args()

        user_request = UserModel.findUser(data['email'])
        
        if not user_request:
            return {
                'code': 406,
                'message': 'User not found'
            }, 406
        
        if UserModel.verify_hash(data['password'], user_request.password):
            access_token = create_access_token(
                identity = data['email'],
                expires_delta = timedelta(hours=1)
            )
            return {
                'access_token': access_token
            }
        else:
            return {'message': 'Wrong credentials'}

class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {
                'code': 200,
                'message': 'Access token has been revoked'
            }, 200
        except Exception as err:
            return {
                'message': 'Something went wrong',
                'error': str(err)
            }, 500      
      
class AllUsers(Resource):
    def __init__(self):
        self.limit = 10
    
    @jwt_required
    def get(self):
        if ('limit' in request.args):
            self.limit = request.args['limit']
        return UserModel.return_all(self.limit)


class UpdateStatusUser(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', help='This field cannot be blank', required=True)
        self.parser.add_argument('email', help='This field cannot be blank', required=True)
        self.parser.add_argument('password', help="This field cannot be blank", required=False)
        self.parser.add_argument('active', help="This field cannot be blank", required=True)
    
    @jwt_required
    def put(self, user_id):
        data = self.parser.parse_args()
        user_request = UserModel.find_by_id(user_id)
        if (user_request):
            active = True if data['active'] == '0' else False
            data['active'] = active
            if (data['password']):
                data['password'] = UserModel.generate_hash(data['password'])
            user_request.update_status_user(**data)
            user_request.save_to_db()
            return {
                'code': 200,
                'status': '{status}'.format(
                    # <valor> = < x > if(True) else < y >
                    status = 'active' if active else 'blocked'
                ),
                'mensage': 'User ID: {id} updated'.format(id=user_id)
            }, 200
        return {
            'code': 406,
            'message': 'user not found'
        }, 406
      
class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }