from django.conf.urls import url
from scrapeApp import views

app_name = 'scrapeApp'

urlpatterns = [

    url(r'^$',views.InputURLPage,name='inputurlpage'),
    url(r'^ScrapeData/$',views.DataPage,name='datapage'),


]
