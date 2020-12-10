from django.shortcuts import render
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import trafilatura

# Create your views here.
def BasePage(request):

    return render(request,'scrapeApp/BasePage.html')

def InputURLPage(request):

    return render(request,'scrapeApp/InputURLPage.html')

def DataPage(request):

    driver = webdriver.Chrome(executable_path =r'C:\Users\raosa\Documents\ATG-WebScraping\chromedriver.exe')

    if request.method == 'POST':

        url = request.POST.get('url')

        url = str(url)

        print('url: ' + url)

        driver.get("<a href=\"https://www.flipkart.com/laptops/\">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

        content = driver.page_source

        soup = BeautifulSoup(content)

        down = trafilatura.fetch_url(url)
        temp_text = trafilatura.extract(down)
        print(soup)


        return render(request,'scrapeApp/DataPage.html')
