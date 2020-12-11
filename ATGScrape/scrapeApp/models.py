from django.db import models

# Create your models here.
class EventModel(models.Model):

    event_name = models.CharField(max_length=300)
    event_date = models.CharField(max_length=300)
    event_price = models.CharField(max_length=30)
    event_venue = models.CharField(max_length=300)
    event_category = models.CharField(max_length=300)

    def __str__(self):

        return self.event_name
