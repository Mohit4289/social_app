from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
            user = token.user
        except Token.DoesNotExist:
            return None
        return (user, token)
