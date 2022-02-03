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
driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
time.sleep(5)

#Navigate to Profile page
driver.find_element(By.XPATH, "//button[@id='menu-button']").click()
driver.find_element(By.XPATH, "//a[text()='Profile']").click()
time.sleep(3)

#Change Password
driver.find_element(By.XPATH, "(//a[contains(text(), 'Change Password')])[2]").click()
time.sleep(4)
driver.find_element(By.ID, "old_password").send_keys("Password12#")
driver.find_element(By.ID, "new_password").send_keys("Password12@")
driver.find_element(By.ID, "confirm_password").send_keys("Password12@")
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(text(),'Save Password')]").click()
time.sleep(5)

driver.close()

