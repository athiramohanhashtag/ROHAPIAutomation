import time


from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Launch driver
s = Service('D:\\HASHTAG\\browsers\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://dev.ringofhires.s3-website.us-east-2.amazonaws.com/")
driver.maximize_window()

#Login
username = "athira@yopmail.com"
password = "Password12@"
driver.find_element(By.XPATH, "//a[text()='Sign In']").click()
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
time.sleep(5)

#Navigate to Profile page
driver.find_element(By.XPATH, "//button[@id='menu-button']").click()
driver.find_element(By.XPATH, "//a[text()='Profile']").click()
time.sleep(3)

#Edit Profile
driver.find_element(By.XPATH, "//input[@type='file']").send_keys("D:\HASHTAG\Images\mghector.jpg")
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]").click()
time.sleep(4)

driver.find_element(By.NAME, "first_name").send_keys(Keys.CONTROL + "a")
driver.find_element(By.NAME, "first_name").send_keys(Keys.DELETE)
driver.find_element(By.NAME, "first_name").send_keys("Athira")
time.sleep(2)
driver.find_element(By.NAME, "last_name").send_keys(Keys.CONTROL + "a")
driver.find_element(By.NAME, "last_name").send_keys(Keys.DELETE)
driver.find_element(By.NAME, "last_name").send_keys("Mohan")
time.sleep(2)

driver.find_element(By.XPATH, "//div[@class='react-select__indicator react-select__dropdown-indicator css-tlfecz-indicatorContainer']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@class='react-select__input']").send_keys(Keys.CONTROL + "a")
driver.find_element(By.XPATH, "//input[@class='react-select__input']").send_keys(Keys.DELETE)
driver.find_element(By.XPATH, "//input[@class='react-select__input']").send_keys("ER Nurse")
driver.find_element(By.XPATH, "//input[@class='react-select__input']").send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='1 (702) 123-4567']").send_keys(Keys.CONTROL + "a")
driver.find_element(By.XPATH, "//input[@placeholder='1 (702) 123-4567']").send_keys(Keys.DELETE)
driver.find_element(By.XPATH, "//div[@role='button']").click()
driver.find_element(By.XPATH, "//span[contains(text(), 'United States')]").click()
driver.find_element(By.XPATH, "//input[@placeholder='1 (702) 123-4567']").send_keys("9072938484")
time.sleep(2)

#driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys(Keys.CONTROL + "a")
#driver.find_element(By.XPATH, "//input[@role='combobox']").send_keys(Keys.DELETE)
driver.find_element(By.XPATH, "/html/body/div/main/div/div[2]/div/form/div[1]/div[5]/div/input").send_keys("Washington Square, Manhattan New York")
driver.find_element(By.XPATH, "/html/body/div/main/div/div[2]/div/form/div[1]/div[5]/div/input").send_keys(Keys.ENTER)
time.sleep(5)
#driver.find_element(By.ID, "state").send_keys(Keys.CONTROL + "a")
#driver.find_element(By.ID, "state").send_keys(Keys.DELETE)
#driver.find_element(By.ID, "state").send_keys("New York")
#time.sleep(1)
#driver.find_element(By.ID, "city").send_keys(Keys.CONTROL + "a")
#driver.find_element(By.ID, "city").send_keys(Keys.DELETE)
#driver.find_element(By.ID, "city").send_keys("New York")
#time.sleep(1)
#driver.find_element(By.ID, "zipcode").send_keys(Keys.CONTROL + "a")
#driver.find_element(By.ID, "zipcode").send_keys(Keys.DELETE)
#driver.find_element(By.ID, "zipcode").send_keys("10012")
driver.execute_script("scrollBy(0, 500);")
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='react-datepicker__input-container']").click()
driver.find_element(By.XPATH, "//div[@class='react-datepicker__input-container']").click()
driver.find_element(By.XPATH, "//input[@class='form_input react-datepicker-ignore-onclickoutside']").clear()
#driver.find_element(By.XPATH, "//div[@class='react-datepicker__input-container']").send_keys(Keys.BACK_SPACE)
#driver.find_element(By.XPATH, "//input[@class='form_input react-datepicker-ignore-onclickoutside']").send_keys("2000-08-01")
#driver.find_element(By.XPATH, "//input[@class='form_input react-datepicker-ignore-onclickoutside']").clear()

#driver.find_element(By.XPATH, "(//div[@class='react-select__indicator react-select__dropdown-indicator css-tlfecz-indicatorContainer'])[2]").click()
#driver.find_element(By.XPATH, "(//div[@class='react-select__indicator react-select__dropdown-indicator css-tlfecz-indicatorContainer'])[2]").send_keys(Keys.CONTROL + "a")
#driver.find_element(By.XPATH, "(//div[@class='react-select__indicator react-select__dropdown-indicator css-tlfecz-indicatorContainer'])[2]").send_keys(Keys.DELETE)
#driver.find_element(By.XPATH, "(//div[@class='react-select__indicator react-select__dropdown-indicator css-tlfecz-indicatorContainer'])[2]").send_keys("Associate Degree in Nursing (ADN)")
time.sleep(3)



slider = driver.find_element(By.XPATH, "//div[contains(@class, 'bg-main bg-main-0')]")
ActionChains(driver).drag_and_drop_by_offset(slider, 0, 0).perform()
ActionChains(driver).click_and_hold(slider).pause(1).move_by_offset(0, 0).release().perform()
time.sleep(3)

ActionChains(driver).drag_and_drop_by_offset(slider, 70, 0).perform()
ActionChains(driver).click_and_hold(slider).pause(1).move_by_offset(70, 0).release().perform()
time.sleep(3)

driver.execute_script("scrollBy(501, 800);")
time.sleep(5)
#driver.find_element(By.XPATH, "/html/body/div/main/div/div[2]/div/form/div[1]/div[13]/div/svg").send_keys("D:\\HASHTAG\\PROJECTS\\RingOfHires\\resume\\file-sample_100kB.doc")
driver.find_element(By.ID, "about_me").send_keys(Keys.CONTROL + "a")
driver.find_element(By.ID, "about_me").send_keys(Keys.DELETE)
driver.find_element(By.ID, "about_me").send_keys("About me")
time.sleep(5)

#driver.find_element(By.XPATH, "(//div[@class='react-select__input-container css-ackcql'])[3]").send_keys(Keys.CONTROL + "a")
#driver.find_element(By.XPATH, "(//div[@class='react-select__input-container css-ackcql'])[3]").send_keys(Keys.DELETE)
#driver.find_element(By.XPATH, "(//div[@class='react-select__input-container css-ackcql'])[3]").send_keys("Teamwork")
#driver.find_element(By.XPATH, "//div[@class='react-select__indicator react-select__dropdown-indicator css-tlfecz-indicatorContainer']").click()
#time.sleep(5)
driver.find_element(By.NAME, "skill_level").send_keys("89")
time.sleep(3)
driver.execute_script("scrollBy(0, 0);")
driver.get_screenshot_as_png("image")
driver.close()