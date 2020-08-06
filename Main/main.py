from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests


page=requests.get('https://www.hindustantimes.com')
soup = BeautifulSoup(page.content,'html.parser')

#options=Options()
#options.add_argument("--headless")
PATH='Main/geckodriver.exe'
#driver=webdriver.Firefox(executable_path=PATH,options=options)

def main_news():
    #driver.get('https://www.thequint.com')
    headlines = soup.find(class_="custom-row border-bottom").get_text()
    #sub_headlines= soup.find(class_="summary _2dXQH").get_text()
    print(headlines)
    #print(sub_headlines)
    #print(driver.find_element_by_xpath('//*[@id="top-story-home"]/div[1]/div[1]/a[2]/h1').text)

main_news()
