from django.contrib import admin
from scrapeApp.models import EventModel,InterestingURLModel,NotInterestingURLModel
from scrapeApp.models import YogaModel,HighModel
# Register your models here.
admin.site.register(EventModel)
admin.site.register(InterestingURLModel)
admin.site.register(NotInterestingURLModel)
admin.site.register(YogaModel)
admin.site.register(HighModel)
