from django.shortcuts import render
import pandas as pd
from scrapeApp.models import EventModel

from bs4 import BeautifulSoup
import requests

# Create your views here.
def BasePage(request):

    return render(request,'scrapeApp/BasePage.html')

def InputURLPage(request):

    return render(request,'scrapeApp/InputURLPage.html')

def DataPage(request):


    if request.method == 'POST':

        url = request.POST.get('url')

        html_text = requests.get(url).text

        soup = BeautifulSoup(html_text, 'lxml')

        events = soup.findAll('div', class_ = 'event-card-details-top')
        price = soup.findAll('div', class_ = 'event-card-container')

        for e,p in zip(events,price):

            name= e.find('span', class_ = 'event-card-name-string').text
            date = e.find('span', class_ = 'event-card-date').text
            price = p.find('div', class_ = 'event-card-price').text
            venue = e.find('span', class_ = 'event-card-venue').text




            # event_date.append(date)
            # event_price.append(price)
            # event_venue.append(venue)

            if EventModel.objects.count() == 0:

                events = EventModel.objects.create(event_name = name, event_date = date, event_price = price, event_venue = venue)
                events.save()

            else:

                names = EventModel.objects.all().values()

                names = list(names)

                temp = []

                for i in range(len(names)):

                    temp.append(names[i]['event_name'])

                if name not in temp:

                    events = EventModel.objects.create(event_name = name, event_date = date, event_price = price, event_venue = venue)
                    events.save()

    events = EventModel.objects.all()

    return render(request,'scrapeApp/DataPage.html',{'events':events})
