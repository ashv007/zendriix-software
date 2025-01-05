from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\driver\selenium\chromedriver.exe")
driver.get("https://facebook.com/")
driver.find_element_by_name("txtUsername").send_keys("9598308354")
driver.find_element_by_id("txtPassword").send_keys("Ashwani@1234")
driver.find_element_by_id("btnLogin").click()

act_title=driver.title
exp_title="facebook"

if act_title==exp_title:
    print("Login test Passed")
else:
    print("Login Test Failed")

driver.close()

