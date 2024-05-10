from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("GitHub")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for search results
    assert "GitHub" in driver.title
    driver.quit()
