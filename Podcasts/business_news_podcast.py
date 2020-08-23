# CREATED BY ANDREW GEORGE ISSAC

#HOW TO USE?
# >RUN THE FUNCTION OF NEWS OF YOUR CHOICE.
# >WAIT FOR THE PODCAST FILE TO OPEN!
 
#NOTE_1: IT TAKES UPTO 10-15sec TO COMPLETE THE PROCESS OF SCRACPING & OPENING THE PODCAST FILE
#NOTE-2: THE PODCAST WILL BE SAVED ON THE SAME FOLDER WHERE THIS .py FILE IS LOCATED.
#NOTE-3: AFTER GETTING DATA, THE PODCAST WILL BE SAVED & OPENED AUTOMATICALLY. NOTHING TO DO MANUALLY!


#COMMENT YOUR SUGGESTIONS/DOUBTS/PROBLEMS @ GitHub


from selenium import webdriver
import smtplib
import time
from gtts import gTTS
import os

PATH='Podcasts/geckodriver.exe'

options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(executable_path=PATH,options=options)



def TOI_business():
    top_stories=''
    lang='en'
    driver.get('https://timesofindia.indiatimes.com/business/india-business') 
    print('driver_optimized')
    i=2
    try:
        while True:
            data=driver.find_element_by_xpath('//*[@id="content"]/li['+str(i)+']/span/a').text
            top_stories=top_stories+'. '+data
            i=i+1
    except:
        pass
    print('scrap_complete')
    output=gTTS(text=top_stories,lang=lang,slow=False)
    output.save('podcast.mp3')
    os.system('start podcast.mp3')

TOI_business()