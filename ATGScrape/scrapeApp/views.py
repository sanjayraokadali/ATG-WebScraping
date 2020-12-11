from django.shortcuts import render
import pandas as pd
from scrapeApp.models import EventModel
import operator
from bs4 import BeautifulSoup
import requests
import csv
# Create your views here.
def BasePage(request):

    return render(request,'scrapeApp/BasePage.html')

def InputURLPage(request):

    return render(request,'scrapeApp/InputURLPage.html')

def DataPage(request):

    events = EventModel.objects.order_by('event_name')
    ordered = sorted(events, key=operator.attrgetter('event_name'))
    flag = True

    if request.method == 'POST':

        url = request.POST.get('url')
        url_li = url.split('/')
        category = ''.join(url_li[len(url_li)-1])

        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        events = soup.findAll('div', class_ = 'event-card-details-top')
        price = soup.findAll('div', class_ = 'event-card-container')

        for e,p in zip(events,price):

            name= e.find('span', class_ = 'event-card-name-string').text
            date = e.find('span', class_ = 'event-card-date').text
            price = p.find('div', class_ = 'event-card-price').text
            venue = e.find('span', class_ = 'event-card-venue').text


            if EventModel.objects.count() == 0:
                events = EventModel.objects.create(event_name = name, event_date = date, event_price = price, event_venue = venue, event_category = category)
                events.save()

            else:
                names = EventModel.objects.all().values()
                names = list(names)
                temp = []

                for i in range(len(names)):
                    temp.append(names[i]['event_name'])
                if name not in temp:
                    flag =False
                    events = EventModel.objects.create(event_name = name, event_date = date, event_price = price, event_venue = venue, event_category = category)
                    events.save()


    if flag == False:

        events = EventModel.objects.order_by('event_name')
        ordered = sorted(events, key=operator.attrgetter('event_name'))
        file = open('event.csv', 'w')
        writer = csv.writer(file)

        writer.writerow(['EVENT NAME','EVENT DATE & TIME','EVENT PRICE,','EVENT VENUE','EVENT CATEGORY'])

        for item in ordered:
            writer.writerow([item.event_name,item.event_date,item.event_price,item.event_venue,item.event_category])
        file.close()

        df = pd.read_csv('event.csv',encoding='utf-8')

        df.to_excel('event.xlsx', index = False, encoding='utf-8')

    return render(request,'scrapeApp/DataPage.html',{'events':ordered})
