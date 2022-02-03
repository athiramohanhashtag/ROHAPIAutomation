
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Launch driver
s = Service('D:\\HASHTAG\\browsers\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://dev.ringofhires.s3-website.us-east-2.amazonaws.com/")
driver.maximize_window()

#Profile
driver.find_element(By.XPATH, "//button[@id='menu-button']").click()
driver.find_element(By.XPATH, "//a[text()='Profile']").click()

driver.find_element(By.NAME, "first_name").send_keys("Arun")
driver.find_element(By.NAME, "last_name").send_keys("Babu")
driver.find_element(By.ID, "react-select-2-listbox").click()

#sel = Select(driver.find_element(By.CLASS_NAME, "react-select__indicator react-select__dropdown-indicator css-tlfecz-indicatorContainer")).click()
time.sleep(3)
#























