from django.conf.urls import url
from scrapeApp import views

app_name = 'scrapeApp'

urlpatterns = [

    url(r'^$',views.InputURLPage,name='inputurlpage'),
    url(r'^CheckURLPage/$',views.CheckURLPage,name='checkurlpage'),
    url(r'^InsiderData/$',views.DataPage,name='datapage'),
    url(r'^ScrapeEvent/$',views.EventsHighURLPage,name='eventhighurlpage'),
    url(r'^CheckEventURLPage/$',views.CheckEventURLPage,name='checkeventurlpage'),
    url(r'^EventHighData/$',views.EventsHighDataPage,name='eventhighdatapage'),
    url(r'^ScrapeYoga/$',views.NaadYogaURLPage,name='naadyogaurlpage'),
    url(r'^CheckYogaURLPage/$',views.CheckYogaURLPage,name='checkyogaurlpage'),
    url(r'^NaadYogaDataPage/$',views.NaadYogaDataPage,name='naadyogadatapage'),
    url(r'^AddToNonPage/$',views.AddToNonPage,name='addtononpage'),
    url(r'^ViewUrlsPage/$',views.ViewURLsPage,name='viewurlspage')


]
