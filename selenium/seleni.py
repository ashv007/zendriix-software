from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="F:/Automation/chromedriver_win32/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login/")
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()
