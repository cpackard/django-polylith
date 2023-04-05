# Third-Party Libraries
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Django Libraries
from rest_framework.request import Request


def email_check(request: Request) -> bool:
    """Returns True if the user's email domain is `nosus.com` and False otherwise."""
    JWT_authenticator = JWTAuthentication()

    # authenticate() verifies and decode the token
    # if token is invalid, it raises an exception and returns 401
    response = JWT_authenticator.authenticate(request)
    if response is not None:
        # unpacking
        user, token = response
        print("this is decoded token claims", token.payload)
        email = token.payload["email"]
        return email.endswith("@nosus.com")
    else:
        print("no token is provided in the header or the header is missing")
        return False


class JwtTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["email"] = user.email
        # ...

        return token
