from models import UserModel
from datetime import timedelta
from flask_restful import Resource, reqparse

from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email', help="This field cannot be blank", required=True)
parser.add_argument('password', help="This field connot be blank", required=True)

class UserRegistry(Resource):
    def post(self):
        data = parser.parse_args()

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
    def post(self):
        data = parser.parse_args()

        user_request = UserModel.find_by_email(data['email'])
        
        if not user_request:
            return {
                'status': 'fail',
                'message': 'User {} does not exist'.format(data['email'])
            }
        
        if UserModel.verify_hash(data['password'], user_request.password):
            access_token = create_access_token(
                identity = data['email'],
                expires_delta = timedelta(hours=1)
            )
            return {
                'message': 'Logged in as {}'.format(user_request.email),
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
            return {'message': 'Access token has been revoked'}, 200
        except:
            return {'message': 'Something went wrong'}, 500      
      
class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()
    
    @jwt_required
    def delete(self):
        return UserModel.delete_all()
      
class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }