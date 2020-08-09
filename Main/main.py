from selenium import webdriver

PATH='geckodriver.exe'

options=webdriver.FirefoxOptions()
options.add_argument('-headless')

driver=webdriver.Firefox(executable_path=PATH,options=options)
driver.get('https://timesofindia.indiatimes.com')

print('--suc')