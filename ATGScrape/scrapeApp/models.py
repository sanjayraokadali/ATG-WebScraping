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

class YogaModel(models.Model):

    name = models.CharField(max_length=264)
    postcode = models.CharField(max_length=264)
    qualification = models.CharField(max_length=264)
    vision = models.TextField()
    link = models.URLField()

    def __str__(self):

        return self.name

class HighModel(models.Model):

    event_name = models.CharField(max_length=264)
    location = models.CharField(max_length=365)
    date = models.CharField(max_length=254)
    category = models.CharField(max_length=243)

    def __str__(self):

        return self.event_name


class InterestingURLModel(models.Model):

    interesting_url = models.URLField()

    def __str__(self):

        return self.interesting_url

class NotInterestingURLModel(models.Model):

    not_interesting_url = models.URLField()

    def __str__(self):

        return self.not_interesting_url
