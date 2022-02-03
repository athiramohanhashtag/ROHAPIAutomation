
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

width = 1024
height = 768

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(width, height)

driver.get('https://google.com')
print('Window size', driver.get_window_size())
# Window size {'width': 1024, 'height': 768}

driver.save_screenshot('screenshot.png')  # <--  Screenshot is saved at different resolution