# import time

from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service

# chrome driver service selenium -160->168 chrome driver

service_obj = Service("E:\TESTING\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/")

# time.sleep(5)
