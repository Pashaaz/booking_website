from abc import ABC

from django.core.validators import RegexValidator
from rest_framework import serializers
from users.models import (
    UserProfile,
    CustomUser,
)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email', 'phone'
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = UserProfile
        fields = (
            'national_number', 'emergency_phone', 'date_of_birth', 'user',
            'card_number', 'bank_account_number', 'bank_sheba_number',
        )


class LoginFirstSerializer(serializers.Serializer):
    phone = serializers.IntegerField(required=True,
                                     validators=[RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.',
                                                                'invalid')])


class LoginSecondSerializer(serializers.Serializer):
    phone = serializers.IntegerField(required=True,
                                     validators=[RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.',
                                                                'invalid')])
    code = serializers.CharField(max_length=6)
