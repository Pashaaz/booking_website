from django.db import models


class Companies(models.Model):
    title = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)


class AbstractTransport(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='transportations')
    origin = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    date = models.DateTimeField()
    boarding_till = models.TimeField()
    depart_time = models.TimeField()
    arrive_time = models.TimeField()
    ticket_enrollment = models.IntegerField()

    class Meta:
        abstract = True


class Flight(AbstractTransport):
    gate = models.CharField(max_length=10)
    flight_type = models.CharField(max_length=20)
    flight = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

    def get_available_tickets(self):
        pass
