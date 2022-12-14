from django.db import models


class AbstractResidence(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    available_times = None
    capacity = models.FloatField()


class Hotels:
    title = models.CharField(max_length=75)
    description = models.TextField()


class HotelRoom(AbstractResidence):
    room_number = models.CharField(max_length=10)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='rooms')


class VillaResidence(AbstractResidence):
    pass


class Facilities(models.Model):
    title = models.CharField(max_length=20)
    residence = models.ManyToManyField(AbstractResidence)


class Locations(models.Model):
    address = models.TextField()
    map_link = models.URLField()


class HotelAvatar(models.Model):
    image = models.ImageField(upload_to='hotels/avatars')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='photos')


class ResidenceAvatar(models.Model):
    image = models.ImageField(upload_to='residences/avatars')
    residence = models.ForeignKey(AbstractResidence, on_delete=models.CASCADE, related_name='photos')
