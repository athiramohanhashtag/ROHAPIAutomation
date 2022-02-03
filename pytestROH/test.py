import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Launch driver


s = Service('D:\\HASHTAG\\browsers\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://dev.ringofhires.s3-website.us-east-2.amazonaws.com/")
driver.maximize_window()



width = 1387
height = 789

chrome_options = Options()

chrome_options.add_argument('window-size=1920x768')

time.sleep(3)
driver.set_window_size(width, height)


print('Window size', driver.get_window_size())


driver.save_screenshot('screenshot2.png')

driver.close()