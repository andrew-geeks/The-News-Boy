# CREATED BY ANDREW GEORGE ISSAC

#HOW TO USE?
# WHEN GMAIL IS USED FOR SENDING DATA, PLEASE MAKE SURE THAT YOU HAVE TURNED ON LESS SECURE APP ACCESS IN THE SECURITY SETTINGS OF YOUR GMAIL ACCOUNT MANAGER!

# RUN THE NEWS FUNCTION WHICH YOU LIKE & THEN RUN THE MAILING FUNCTION!

#NOTE: IT TAKES UPTO 40-50sec TO COMPLETE THE PROCESS OF SCRACPING & SENDING.
#NOTE: THE RECIEPIENT MAIL ADDRESS CAN BE ANY MAIL FROM ANY PROVIDER!
#COMMENT YOUR SUGGESTIONS, DOUBTS, PROBLEMS @ GitHub


from selenium import webdriver
import smtplib
import time

PATH='Mailing_news/geckodriver.exe'

options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(executable_path=PATH,options=options)
headlines=''
top_stories=[]
news_name=''


def TOI_business():
    global headlines
    global top_stories
    global news_name
    news_name='Times Of India Business'
    driver.get('https://timesofindia.indiatimes.com/business/india-business') 
    print('driver_optimized')
    headlines=driver.find_element_by_xpath('//*[@id="content"]/li[1]/span[1]/a').text
    i=2
    try:
        while True:
            data=driver.find_element_by_xpath('//*[@id="content"]/li['+str(i)+']/span/a').text
            top_stories.append(str(i-1)+'.'+' '+data+'\n')
            i=i+1
    except:
        pass
    print('scrap_complete')






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

TOI_business()
gmail_send()