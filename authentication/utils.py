from datetime import datetime, timedelta
from django.conf import settings
import jwt

def generate_jwt_token(user):
    expiration = datetime.utcnow() + settings.JWT_AUTH['JWT_EXPIRATION_DELTA']
    token = jwt.encode(
        {
            'user_id': user.id,
            'exp': expiration,
        },
        settings.JWT_AUTH['JWT_SECRET_KEY'],
        algorithm='HS256'
    )
    return token.decode('utf-8')

def decode_jwt_token(token):
    try:
        decoded_token = jwt.decode(
            token,
            settings.JWT_AUTH['JWT_SECRET_KEY'],
            algorithms=['HS256']
        )
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
