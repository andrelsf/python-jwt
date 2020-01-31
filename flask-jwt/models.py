from run import db
#from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # active = db.Column(db.Boolean(), default=False, nullable=False)
    # create_at = db.Column(db.DateTime(), default=datetime.now)
    # update_at = db.Column(
    #     db.DateTime(), default=datetime.now, onupdate=datetime.now
    # )

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email = email).first()

    @classmethod
    def return_all(cls):
        def to_json(user):
            return {
                'email': user.email,
                'password': user.password
            }
        return {'users': list(map(lambda user: to_json(user), UserModel.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            result = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(result)}
        except:
            return {'message': 'something went wrong'}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()