from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.IntegerField(unique=True, validators=[RegexValidator(
        regex='09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}',
        message='Please enter a valid number (09...)')])
    password = models.CharField(max_length=20,
                                validators=[RegexValidator(regex='^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                                                           message='Password must contain at least 8 characters,'
                                                                   ' 1 number, and 1 letter'
                                                           )])

    user_profile = models.OneToOneField('UserProfile', on_delete=models.CASCADE)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["password"]


class UserProfile(models.Model):
    national_number = models.IntegerField(blank=True, null=True)
    emergency_phone = models.IntegerField(blank=True, null=True, validators=[RegexValidator(
        regex='09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}' or '^0[0-9]{2,}[0-9]{7,}$')
    ]
                                          )
    date_of_birth = models.DateField(blank=True, null=True)

    card_number = models.IntegerField(blank=True, null=True)
    bank_account_number = models.IntegerField(blank=True, null=True)
    bank_sheba_number = models.IntegerField(blank=True, null=True)
