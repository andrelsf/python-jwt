from models import UserModel
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
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
                'message': 'User {} does not exist'.format(data['email'])
            }
        
        if UserModel.verify_hash(data['password'], user_request.password):
            return {
                'message': 'Logged in as {}'.format(user_request.email)
            }
        else:
            return {'message': 'Wrong credentials'}
      
      
class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}
      
      
class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()
      
      
class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }