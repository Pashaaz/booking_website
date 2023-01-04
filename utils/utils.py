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


def update_price(update_number, model):

    for obj in model.objects.all():
        addition_or_subtraction_num = obj.price * update_number / 100
        obj.price = obj.price + addition_or_subtraction_num

        obj.save()
