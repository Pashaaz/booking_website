from django.db import models


class Facilities(models.Model):
    title = models.CharField(max_length=20)


class Locations(models.Model):
    address = models.TextField()
    map_link = models.URLField()


class AbstractResidence(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    available_times = None
    capacity = models.FloatField()
    facilities = models.ManyToManyField(Facilities)


class Hotels(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='hotel_locations')


class HotelRoom(AbstractResidence):
    room_number = models.CharField(max_length=10)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='rooms')


class VillaResidence(AbstractResidence):
    location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='villa_locations')


class HotelAvatar(models.Model):
    image = models.ImageField(upload_to='hotels/avatars')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='photos')


class ResidenceAvatar(models.Model):
    image = models.ImageField(upload_to='residences/avatars')
    residence = models.ForeignKey(AbstractResidence, on_delete=models.CASCADE, related_name='photos')
