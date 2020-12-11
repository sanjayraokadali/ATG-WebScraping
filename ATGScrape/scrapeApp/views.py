from django.shortcuts import render
import pandas as pd

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

        event_name = []
        event_price = []
        event_date = []

        for e,p in zip(events,price):

            name= e.find('span', class_ = 'event-card-name-string').text
            date = e.find('span', class_ = 'event-card-date').text
            price = p.find('div', class_ = 'event-card-price').text

            event_name.append(name)
            event_date.append(date)
            event_price.append(price)


        events.append(event_name)
        events.append(event_date)
        events.append(event_price)

        print(events)

    return render(request,'scrapeApp/DataPage.html',{'events':events})
