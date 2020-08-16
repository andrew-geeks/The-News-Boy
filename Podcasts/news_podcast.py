from gtts import gTTS
import os
from bs4 import BeautifulSoup 
import requests


def TOI(): #Times_Of_India
    lang='en'
    page=requests.get('https://timesofindia.indiatimes.com')
    soup = BeautifulSoup(page.content,'html.parser')
    data = soup.find(class_="top-story").get_text()
    output=gTTS(text=data,lang=lang,slow=False)
    output.save('podcast.mp3')
    os.system('start podcast.mp3')


def blmg_qnt(): #bloomberg_quint
    lang='en'
    page=requests.get('https://www.bloombergquint.com')
    soup = BeautifulSoup(page.content,'html.parser')
    data = soup.find(class_="three-col-nine-stories-m__stories_container__12HEv").get_text()
    output=gTTS(text=data,lang=lang,slow=False)
    output.save('podcast.mp3')
    os.system('start podcast.mp3')


def India_Today(): 
    lang='en'
    page=requests.get('https://www.indiatoday.in')
    soup = BeautifulSoup(page.content,'html.parser')
    data = soup.find(class_="itg-widget-child tab-data tab-data-1").get_text()
    output=gTTS(text=data,lang=lang,slow=False)
    output.save('podcast.mp3') 
    os.system('start podcast.mp3')


def Ind_Exprs():
    lang='en'
    page=requests.get('https://indianexpress.com/')
    soup = BeautifulSoup(page.content,'html.parser')
    data = soup.find(class_="top-news").get_text()
    output=gTTS(text=data,lang=lang,slow=False)
    output.save('podcast.mp3')
    os.system('start podcast.mp3')


Ind_Exprs()