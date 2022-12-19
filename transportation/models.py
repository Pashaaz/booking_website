from django.db import models


class Companies(models.Model):
    title = models.CharField(max_length=100)


class AbstractTransport(models.Model):
    TIME_CHOICES = (
         (1, '00:00'), (13, '06:00'), (25, '12:00'), (37, '18:00'),
         (2, '00:30'), (14, '06:30'), (26, '12:30'), (38, '18:30'),
         (3, '01:00'), (15, '07:00'), (27, '13:00'), (39, '19:00'),
         (4, '01:30'), (16, '07:30'), (28, '13:30'), (40, '19:30'),
         (5, '02:00'), (17, '08:00'), (29, '14:00'), (41, '20:00'),
         (6, '02:30'), (18, '08:30'), (30, '14:30'), (42, '20:30'),
         (7, '03:00'), (19, '09:00'), (31, '15:00'), (43, '21:00'),
         (8, '03:30'), (20, '09:30'), (32, '15:30'), (44, '21:30'),
         (9, '04:00'), (21, '10:00'), (33, '16:00'), (45, '22:00'),
        (10, '04:30'), (22, '10:30'), (34, '16:30'), (46, '22:30'),
        (11, '05:00'), (23, '11:00'), (35, '17:00'), (47, '23:00'),
        (12, '05:30'), (24, '11:30'), (36, '17:30'), (48, '23:30'),
    )

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='transportations')
    origin = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    date = models.DateTimeField()
    boarding_till = models.IntegerField(choices=TIME_CHOICES)
    depart_time = models.IntegerField(choices=TIME_CHOICES)
    arrive_time = models.IntegerField(choices=TIME_CHOICES)

    class Meta:
        abstract = True


class AirlineTransport(AbstractTransport):
    gate = models.CharField(max_length=10)
    flight = models.CharField(max_length=50)


class AirlineTicket(models.Model):
    seat = models.CharField(max_length=10)
    airline = models.ForeignKey(AirlineTransport, on_delete=models.CASCADE, related_name='tickets')
