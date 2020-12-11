from django.conf.urls import url
from scrapeApp import views

app_name = 'scrapeApp'

urlpatterns = [

    url(r'^$',views.InputURLPage,name='inputurlpage'),
    url(r'^InsiderData/$',views.DataPage,name='datapage'),
    url(r'^ScrapeData/$',views.EventsHighURLPage,name='eventhighurlpage'),
    url(r'^EventHighData/$',views.EventsHighDataPage,name='evenhighdatapage'),
    url(r'^ScrapeData/$',views.NaadYogaURLPage,name='naadyogaurlpage'),
    url(r'^NaadYogaData/$',views.NaadYogaDataPage,name='naadyogadatapage'),


]
