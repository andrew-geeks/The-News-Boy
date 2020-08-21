# CREATED BY ANDREW GEORGE ISSAC

#HOW TO USE?
# WHEN GMAIL IS USED FOR SENDING DATA, PLEASE MAKE SURE THAT YOU HAVE TURNED ON LESS SECURE APP ACCESS IN THE SECURITY SETTINGS OF YOUR GMAIL ACCOUNT MANAGER!

# RUN THE NEWS FUNCTION WHICH YOU LIKE & THEN RUN THE MAILING FUNCTION!

#NOTE: IT TAKES UPTO 40-50sec TO COMPLETE THE PROCESS OF SCRACPING & SENDING.
#COMMENT YOUR SUGGESTIONS, DOUBTS, PROBLEMS @ GitHub




from selenium import webdriver
import smtplib


PATH="Mailing_news/geckodriver.exe"

options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(executable_path=PATH,options=options)



def TOI(): #Times_of_India
    global top_stories
    global headlines
    global news_name
    top_stories=[]
    news_name='TimesOfIndia'
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
    global news_name
    news_name='IndiaToday'
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
    global news_name
    news_name='IndianExpress'
    top_stories=[]
    driver.get('https://indianexpress.com')
    print('driver_optimized')
    headlines=driver.find_element_by_xpath('//*[@id="HP_TOP_NEWS_STORIES"]/div[1]/div[1]/div[1]/h2/a').text
    try:
        for i in range(1,6):
            stry=driver.find_element_by_xpath('//*[@id="HP_TOP_NEWS_STORIES"]/div[2]/div/ul/li['+str(i)+']/h3/a').text
            top_stories.append(str(i)+'. '+stry+'\n')
    except:
        pass
    print('--scrap_complete')



def gmail_send():  #gmail_function
    SUBJECT='The News Boy! '+news_name
    BODY='Breaking News:'+headlines+'\n'+'\n--Top Stories--\n'
    for n in range(len(top_stories)):
        BODY=BODY+top_stories[n]
    BODY=BODY+'\n'+'\n'+'With Love,'+'\n'+'NewsBoy_Initiative(By Andrew)'
    message = 'Subject: {}\n\n{}'.format(SUBJECT, BODY).encode('utf-8')
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login('your_gmail','your_gmail_password')
    mail.sendmail('your_gmail','reciepient_mail_address',message)
    mail.close()
    print('mailing complete!')


def outlook_send():  #outlook_function
    SUBJECT='The News Boy! '+news_name
    BODY='Breaking News:'+headlines+'\n'+'\n--Top Stories--\n'
    for n in range(len(top_stories)):
        BODY=BODY+top_stories[n]
    BODY=BODY+'\n'+'\n'+'With Love,'+'\n'+'NewsBoy_Initiative(By Andrew)'
    message = 'Subject: {}\n\n{}'.format(SUBJECT, BODY).encode('utf-8')
    mail=smtplib.SMTP('smtp-mail.outlook.com',587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login('your_outlook_mail','your_outlook_mail_password')
   
    mail.sendmail('your_outlook_mail','recipient_email_address',message)
    mail.close()
    print('mailing complete!')




