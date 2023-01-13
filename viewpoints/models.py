from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from residence.models import Hotels
from transportation.models import Companies


class AbstractComment(models.Model):
    STATUS_CHOICES = (
        (1, 'Created'),
        (2, 'Approved'),
        (3, 'Rejected'),
        (4, 'Deleted')
    )

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


    comment_body = models.TextField()

    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)


    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractRating(models.Model):

    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HotelComment(AbstractComment):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='hotel_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='%(class)ss')
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='validated_%(class)ss')


class CompanyComment(AbstractComment):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='company_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='%(class)ss')
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='validated_%(class)ss')


class HotelRating(AbstractRating):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='hotel_ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user_hotel_ratings')

    class Meta:
        constraints = [models.UniqueConstraint(fields=('user', 'hotel'), name='unique_user_hotel')]


class CompanyRating(AbstractRating):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='company_ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user_company_ratings')

    class Meta:
        constraints = [models.UniqueConstraint(fields=('user', 'company'), name='unique_user_company')]
