from selenium import webdriver
import smtplib

PATH='Main/geckodriver.exe'

options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(executable_path=PATH,options=options)
driver.get('https://timesofindia.indiatimes.com')
print('driver_optimized')
headlines=driver.find_element_by_xpath('//*[@id="featuredstory"]/h2/a').text
top_stories=[]

i=1
try:
    while True:
        stry=driver.find_element_by_xpath('//*[@id="content"]/div/div[6]/ul/li['+str(i)+']/a[1]').text
        top_stories.append('\n'+str(i)+'. '+stry)
        i=i+1
        
except:
    pass

print('--scrap_complete')
for i in range(len(top_stories)):
    print(top_stories[i])
def send():
    content='hello'
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('yourgmail','gmail_password')
    subject='The News Boy!'
    body='Breaking News:'+headlines+'\n'+'\n--Top Stories--\n'

    for n in range(len(top_stories)):
        body=body+top_stories[n]

    msg=f'Subject: {subject}\n\n{body}'
    mail.sendmail('yourgmail','recipient_mail',msg)
    mail.close()
    print('mailing complete!')

send()