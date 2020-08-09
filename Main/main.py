from selenium import webdriver

PATH='Main/geckodriver.exe'

options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(executable_path=PATH,options=options)
driver.get('https://timesofindia.indiatimes.com')

headlines=driver.find_element_by_xpath('//*[@id="featuredstory"]/h2/a').text
top_stories=[]

i=1
try:
    while True:
        stry=driver.find_element_by_xpath('//*[@id="content"]/div/div[6]/ul/li['+str(i)+']/a[1]').text
        i=i+1
        top_stories.append(stry)
except:
    pass
#//*[@id="content"]/div/div[6]/ul/li[1]/a[1] #//*[@id="content"]/div/div[6]/ul/li[2]/a

for i in range(len(top_stories)):
    print(top_stories[i])