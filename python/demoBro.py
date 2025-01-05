import time

from attr import attributes
from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from demoBrower import driver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID,Xpath,CSSSelector,Classname,name,linkText

driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
# Xpath - //tagname[@attribute='value']-> //input[@type='submit']
# CSS - tagname[attribute='value']->//input[@type='submit'], #id, .classname

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# message =driver.find_element(By.CLASS_NAME,"alert-success").text
# print(message)
# assert "Succes" in message

#Static DropDown
dropdown =Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)



driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Succes" in message




driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()



time.sleep(5)


# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)