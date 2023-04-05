# Django Libraries
from rest_framework.request import Request

# Polylith Bricks
from cpackard.authentication import core


def email_check(request: Request) -> bool:
    return core.email_check(request)


class JwtTokenObtainPairSerializer(core.JwtTokenObtainPairSerializer):
    pass


class JWTAuthentication(core.JWTAuthentication):
    pass
