from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
options.add_argument("--headless")
PATH='Main/geckodriver.exe'
driver=webdriver.Firefox(executable_path=PATH,options=options)


