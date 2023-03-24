from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 
import os # Store twitter username and password as env. variables

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
website = "https://www.twitter.com"
path = "C:/Users/harsh/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(path,options=options,service=Service(ChromeDriverManager().install()))
driver.get(website)
driver.maximize_window()

# Wait of 6 seconds to let the page load the content
time.sleep(6)  # this time might vary depending on your computer
# Locating username and password inputs and sending text to the inputs
# Username
username = driver.find_element_by_xpath('//input[@autocomplete ="username"]')
username.send_keys(os.environ.get("TWITTER_USER"))
# Clicking on "next" button
next_button = driver.find_element_by_xpath('//div[@role="button"]//span[text()="Next"]')
next_button.click()
# Wait of 2 seconds after clicking button
time.sleep(2)
# Password
password = driver.find_element_by_xpath('//input[@autocomplete ="current-password"]')
password.send_keys(os.environ.get("TWITTER_PASS"))
# Locating login button and then clicking on it
login_button = driver.find_element_by_xpath('//div[@role="button"]//span[text()="Log in"]')
login_button.click()
driver.quit()
