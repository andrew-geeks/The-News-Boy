from bs4 import BeautifulSoup
import requests


page=requests.get('https://www.indiatoday.in/')
soup = BeautifulSoup(page.content,'html.parser')


PATH='Main/geckodriver.exe'

def main_news():
    
    headlines = soup.find(class_="home-page-feature-1708626").get_text()
    #print(headlines)
    top_stories=soup.find(class_="widget-wrapper top_stories_ordering").get_text()
    
    print(top_stories)
    

main_news()
