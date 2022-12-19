from django.db import models


class Companies(models.Model):
    title = models.CharField(max_length=100)


class AbstractTransport(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='transportations')
    origin = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    date = models.DateTimeField()
    boarding_till = models.TimeField()
    depart_time = models.TimeField()
    arrive_time = models.TimeField()

    class Meta:
        abstract = True


class AirlineTransport(AbstractTransport):
    gate = models.CharField(max_length=10)
    flight_type = models.CharField(max_length=20)
    flight = models.CharField(max_length=50)


class AirlineTicket(models.Model):
    seat = models.CharField(max_length=10)
    airline = models.ForeignKey(AirlineTransport, on_delete=models.CASCADE, related_name='tickets')
