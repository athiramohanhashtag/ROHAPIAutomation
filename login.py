import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

#Profile
driver.find_element(By.XPATH, "//button[@id='menu-button']").click()
driver.find_element(By.XPATH, "//a[text()='Profile']").click()

driver.find_element(By.NAME, "first_name").send_keys("Arun")
driver.find_element(By.NAME, "last_name").send_keys("Babu")
driver.find_element(By.ID, "react-select-2-input").click()

driver.find_element(By.ID, "react-select-2-listbox").click()
time.sleep(2)
#driver.find_element(By.XPATH, "//div[contains(text(), 'Anesthesiology')]").click()
#time.sleep(2)
driver.find_element(By.XPATH, "//div[contains(text(), 'Nurse Midwife or Midwife')]").click()
#actions = ActionChains(driver)
#actions.move_to_element(element).perform()

#driver.find_element(By.XPATH, "//div[contains(text(), 'Nurse Midwife or Midwife')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//body/div[@id='root']/main[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[5]/div[1]/input[1]").send_keys("Lake Placid")
driver.find_element(By.XPATH,  "//input[value='lake Placid']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.find_element(By.CLASS_NAME, "form_input react-datepicker-ignore-onclickoutside").click()
# driver.close()





































