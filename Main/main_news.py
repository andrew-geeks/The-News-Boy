from selenium import webdriver
import smtplib


PATH='Main/geckodriver.exe'

options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(executable_path=PATH,options=options)

headlines=''
top_stories=[]


def TOI(): #Times_of_India
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
    for i in range(len(top_stories)):
        print(top_stories[i])
   


india_today()

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
    mail.login('your_gmail','gmail_password')
   
    mail.sendmail('your_gmail','recipient_email_address',message)
    mail.close()
    print('mailing complete!')

#send()