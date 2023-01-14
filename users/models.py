from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, validators=[RegexValidator(
        regex='09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}',
        message='Please enter a valid number (09...)')])
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    iri_to = models.CharField(max_length=3, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone"]


class UserProfile(models.Model):
    national_number = models.IntegerField(blank=True, null=True)
    emergency_phone = models.IntegerField(blank=True, null=True, validators=[RegexValidator(
        regex='09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}' or '^0[0-9]{2,}[0-9]{7,}$')
    ]
                                          )
    date_of_birth = models.DateField(blank=True, null=True)

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    card_number = models.IntegerField(blank=True, null=True)
    bank_account_number = models.IntegerField(blank=True, null=True)
    bank_sheba_number = models.IntegerField(blank=True, null=True)
