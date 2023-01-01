from random import randint

from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def otp_gen():
    otp = ''

    for i in range(6):
        otp += str(randint(0, 9))

    return otp
