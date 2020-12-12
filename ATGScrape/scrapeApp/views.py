from django.shortcuts import render
import pandas as pd
from scrapeApp.models import EventModel
import operator
from bs4 import BeautifulSoup
import requests
import csv
from scrapeApp.models import InterestingURLModel,NotInterestingURLModel
from scrapeApp.models import YogaModel
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

        data = InterestingURLModel.objects.create(interesting_url = url)
        data.save()

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
        file = open('insider_event.csv', 'w', encoding='utf-8')
        writer = csv.writer(file)

        writer.writerow(['EVENT NAME','EVENT DATE & TIME','EVENT PRICE','EVENT VENUE','EVENT CATEGORY'])

        for item in ordered:
            writer.writerow([item.event_name,item.event_date,item.event_price,item.event_venue,item.event_category])
        file.close()

        df = pd.read_csv('insider_event.csv', encoding='utf-8')

        df.to_excel('insider_event.xlsx', index = False, encoding='utf-8')

    return render(request,'scrapeApp/DataPage.html',{'events':ordered})


def CheckURLPage(request):

    if request.method == 'POST':

        url = request.POST.get('url')

    return render(request,'scrapeApp/CheckURLPage.html',{'url':url})

def CheckEventURLPage(request):

    if request.method == 'POST':

        url = request.POST.get('url')

    return render(request,'scrapeApp/CheckEventURLPage.html',{'url':url})

def AddToNonPage(request):

    if request.method == 'POST':

        take_url = request.POST.get('take_url')

        data = NotInterestingURLModel.objects.create(not_interesting_url = take_url)

        data.save()

    return render(request,'scrapeApp/AddToNonPage.html')



def EventsHighURLPage(request):

    return render(request,'scrapeApp/EventsHighURLPage.html')


def EventsHighDataPage(request):

    url = request.POST.get('url')

    data = InterestingURLModel.objects.create(interesting_url = url)
    data.save()


    url_li = url.split('/')
    location = ''.join(url_li[len(url_li)-1])

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    events = soup.find_all('div', class_ = 'p-lr-sm-16 t-container browse-events-wrp')


    for e in events:

        event_name = e.find('div', class_='truncate f-s-16 f-s-sm-12 l-h-1p5 color-dark-grey' ).text

        print(event_name)



    return render(request,'scrapeApp/EventsHighDataPage.html')


def NaadYogaURLPage(request):

    return render(request,'scrapeApp/NaadYogaURLPage.html')

def CheckYogaURLPage(request):

    if request.method == 'POST':

        url = request.POST.get('url')

    return render(request,'scrapeApp/CheckYogaURLPage.html',{'url':url})


def NaadYogaDataPage(request):

    yoga = YogaModel.objects.order_by('name')
    ordered = sorted(yoga, key=operator.attrgetter('name'))
    flag=True

    if request.method == 'POST':

        url = request.POST.get('url')

        data = InterestingURLModel.objects.create(interesting_url = url)
        data.save()



        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')

        names = soup.findAll('td', class_ = 'column-1')
        postcode = soup.findAll('td', class_ = 'column-3')
        qualification = soup.findAll('td', class_ = 'column-4')
        vision = soup.findAll('td', class_ = 'column-5')
        link = soup.findAll('td', class_ = 'column-6')

        for e,p,q,v,l in zip(names,postcode,qualification,vision,link):

            name = e.text
            postcode = p.text
            qualification = q.text
            vision = v.text
            link = l.text

            if YogaModel.objects.count == 0:

                yoga = YogaModel.objects.create(name = name, postcode = postcode, qualification = qualification, vision = vision, link = link)
                yoga.save()

            else:
                names = YogaModel.objects.all().values()
                names = list(names)
                temp = []

                for i in range(len(names)):
                    temp.append(names[i]['name'])

                if name not in temp:
                    flag =False
                    yoga = YogaModel.objects.create(name = name, postcode = postcode, qualification = qualification, vision = vision, link = link)
                    yoga.save()


    if flag == False:

        yoga = YogaModel.objects.order_by('name')
        ordered = sorted(yoga, key=operator.attrgetter('name'))
        yoga_file = open('yoga_event.csv', 'w', encoding='utf-8')
        writer = csv.writer(yoga_file)

        writer.writerow(['INSTRUCTOR NAME','POSTCODE','QUALIFICATION','VISION','LINK'])

        for item in ordered:
            writer.writerow([item.name,item.postcode,item.qualification,item.vision,item.link])

        yoga_file.close()

        df = pd.read_csv('yoga_event.csv', encoding='utf-8')

        df.to_excel('yoga_event.xlsx', index = False, encoding='utf-8')


    return render(request,'scrapeApp/NaadYogaDataPage.html',{'yoga':ordered})

def ViewURLsPage(request):

    int_url = InterestingURLModel.objects.all()
    not_int = NotInterestingURLModel.objects.all()

    return render(request,'scrapeApp/ViewURLsPage.html',{'int':int_url,'not':not_int})
