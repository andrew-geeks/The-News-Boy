from selenium import webdriver
import smtplib
import time

PATH='Mailing_news/geckodriver.exe'

options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(executable_path=PATH,options=options)
headlines=''
top_stories=[]

def TOI_business():
    global headlines
    global top_stories
    driver.get('https://timesofindia.indiatimes.com/business/india-business') 
    print('driver_optimized')
    headlines=driver.find_element_by_xpath('//*[@id="content"]/li[1]/span[1]/a').text
    
    i=2
    try:
        while True:
            data=driver.find_element_by_xpath('//*[@id="content"]/li['+str(i)+']/span/a').text
            top_stories.append(str(i-1)+'.'+' '+data)
            i=i+1
    except:
        pass





#//*[@id="content"]/li[2]/span/a
#//*[@id="content"]/li[3]/span/a