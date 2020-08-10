# CREATED BY ANDREW GEORGE ISSAC

#HOW TO USE?
# RUN THE NEWS FUNCTION WHICH YOU LIKE & THEN RUN THE MAILING FUNCTION
#COMMENT YOUR SUGGESTIONS, DOUBTS, PROBLEMS @ GitHub




from selenium import webdriver
import smtplib


PATH='Main/geckodriver.exe'

options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(executable_path=PATH,options=options)



def TOI(): #Times_of_India
    global top_stories
    global headlines
    top_stories=[]
    driver.get('https://timesofindia.indiatimes.com')
    print('driver_optimized')
    headlines=driver.find_element_by_xpath('//*[@id="featuredstory"]/h2/a').text
    
    i=1
    try:
        while True:
            stry=driver.find_element_by_xpath('//*[@id="content"]/div/div[6]/ul/li['+str(i)+']/a[1]').text
            top_stories.append('\n'+str(i)+'. '+stry)
            i=i+1    
    except:
        pass
    print('--scrap_complete')


def india_today(): #India_Today
    global top_stories
    global headlines
    top_stories=[]
    driver.get('https://www.indiatoday.in/')
    print('driver_optimized')
    headlines=driver.find_element_by_xpath('//*[@id="block-itg-widget-home-page-feature"]/div/div[1]/h2/a').text
    
    try:
        for i in range(1,6):
            stry=driver.find_element_by_xpath('//*[@id="block-itg-widget-top-stories-ordering"]/ul/li['+str(i)+']/a').text
            top_stories.append(str(i)+'. '+stry+'\n')
    except:
        pass
    print('--scrap_complete')
   

def indian_express(): #Indian_Express
    global top_stories
    global headlines
    top_stories=[]
    driver.get('https://indianexpress.com')
    print('driver_optimized')
    headlines=driver.find_element_by_xpath('//*[@id="HP_TOP_NEWS_STORIES"]/div[1]/div/div[2]/h2/a').text
    try:
        for i in range(1,6):
            stry=driver.find_element_by_xpath('//*[@id="HP_TOP_NEWS_STORIES"]/div[2]/div/ul/li['+str(i)+']/h3/a').text
            top_stories.append(str(i)+'. '+stry+'\n')
    except:
        pass
    print('--scrap_complete')





def send(): #mailing_function
    SUBJECT='The News Boy!'
    BODY='Breaking News:'+headlines+'\n'+'\n--Top Stories--\n'
    for n in range(len(top_stories)):
        BODY=BODY+top_stories[n]
    message = 'Subject: {}\n\n{}'.format(SUBJECT, BODY).encode('utf-8')
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login('your_gmail','your_gmail_password')
   
    mail.sendmail('your_gmail','receipient_email',message)
    mail.close()
    print('mailing complete!')

