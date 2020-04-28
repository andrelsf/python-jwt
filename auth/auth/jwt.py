from run import jwt
from models import RevokedTokenModel

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
    return RevokedTokenModel.is_jti_blacklisted(jti)