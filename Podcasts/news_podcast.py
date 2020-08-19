# CREATED BY ANDREW GEORGE ISSAC

#HOW TO USE?
# >RUN THE FUNCTION OF NEWS OF YOUR CHOICE.
# >WAIT FOR THE PODCAST FILE TO OPEN!
 
#NOTE_1: IT TAKES UPTO 5-7sec TO COMPLETE THE PROCESS OF SCRACPING & OPENING THE PODCAST FILE
#NOTE-2: THE PODCAST WILL BE SAVED ON THE SAME FOLDER WHERE THIS .py FILE IS LOCATED.
#NOTE-3: AFTER GETTING DATA, THE PODCAST WILL BE SAVED & OPENED AUTOMATICALLY. NOTHING TO DO MANUALLY!


#COMMENT YOUR SUGGESTIONS/DOUBTS/PROBLEMS @ GitHub


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


def India_Today(): #India_Today
    lang='en'
    page=requests.get('https://www.indiatoday.in')
    soup = BeautifulSoup(page.content,'html.parser')
    data = soup.find(class_="itg-widget-child tab-data tab-data-1").get_text()
    output=gTTS(text=data,lang=lang,slow=False)
    output.save('podcast.mp3') 
    os.system('start podcast.mp3')


def Ind_Exprs(): #Indian_Express
    lang='en'
    page=requests.get('https://indianexpress.com/')
    soup = BeautifulSoup(page.content,'html.parser')
    data = soup.find(class_="top-news").get_text()
    output=gTTS(text=data,lang=lang,slow=False)
    output.save('podcast.mp3')
    os.system('start podcast.mp3')


