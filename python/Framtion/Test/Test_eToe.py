import pytest
from  selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestOne:
    def test_e2e(self,setup):
        driver = webdriver.Chrome()
        driver.get("https://qaclickacademy.github.io/protocommerce/")
        driver.maximize_window()
        driver.find_element_by_css_selector("a[href*='shop']").click()
        cards = driver.find_element_by_css_selector(".card-title a")
        i = -1
        for card in cards:
            i = i +1
            cardText = card.text
