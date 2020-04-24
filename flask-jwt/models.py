from run import db
from uuid import uuid4
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy.dialects.postgresql import UUID

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    createAt = db.Column(db.DateTime(), default=datetime.now)
    updateAt = db.Column(
         db.DateTime(), default=datetime.now, onupdate=datetime.now
    )

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
    def findUser(cls, email):
        return cls.query.filter_by(email = email, active = True).first()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def return_all(cls):
        def to_json(user):
            return {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'active': user.active,
                'createAt': str(user.createAt),
                'updateAt': str(user.updateAt)
            }
        return {'users': list(map(lambda user: to_json(user), UserModel.query.all()))}

    def update_status_user(self, active):
        self.active = active

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

"""
    Revoked Token Model
        Methods:
            add(): adds token to the database
            is_jti_blacklisted(): check if token is revoked
"""
class RevokedTokenModel(db.Model):

    __tablename__ = 'revoked_tokens'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)