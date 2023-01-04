from django.db import models


# ----------------------------------------------- Abstract models ------------------------------------------------------
class AbstractResidence(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    available_times = None
    capacity = models.FloatField()
    facilities = models.ManyToManyField('Facilities')

    class Meta:
        abstract = True


# ------------------------------------------- End of abstract models ---------------------------------------------------


# ------------------------------------------------ Simple models -------------------------------------------------------
class Facilities(models.Model):
    title = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)


class Locations(models.Model):
    address = models.TextField()
    map_link = models.URLField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)


# -------------------------------------------- End of simple models ----------------------------------------------------


# ------------------------------------------------ Main models ---------------------------------------------------------
class Hotels(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)


class HotelRoom(AbstractResidence):
    room_number = models.CharField(max_length=10)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='rooms')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)


# --------------------------------------------- End of main models -----------------------------------------------------


# ----------------------------------------------- Avatar models --------------------------------------------------------
class HotelAvatar(models.Model):
    image = models.ImageField(upload_to='hotels/avatars')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='photos')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)


class HotelRoomAvatar(models.Model):
    image = models.ImageField(upload_to='residences/avatars')
    residence = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='photos')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

# -------------------------------------------- End of avatar models ----------------------------------------------------
