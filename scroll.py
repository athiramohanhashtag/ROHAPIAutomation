import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#Launch driver
s = Service('D:\\HASHTAG\\browsers\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://dev.ringofhires.s3-website.us-east-2.amazonaws.com/")
driver.maximize_window()

#Login
username = "athira@yopmail.com"
password = "Password12#"
driver.find_element(By.XPATH, "//a[text()='Sign In']").click()
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
#driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

driver.execute_script("scrollBy(0, 200);")
time.sleep(3)
#driver.execute_script("scrollBy(0, -200);")
#time.sleep(3)
driver.execute_script("scrollBy(201, 500);")
time.sleep(3)


driver.close()

