# Self-Note: Infinite Scrolling Is Similar To Lazy Loading,
# Infinite Scroll loads the entire resources of the next page as soon as the user nears the page end, thus removing the need to click to reach the next page. Lazy Loading requests just the necessary resources only when they are demanded.
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
website = "https://twitter.com/TwitterSupport/status/1415364740583395328"
path = "C:/Users/harsh/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(path,options=options,service=Service(ChromeDriverManager().install()))
driver.get(website)
driver.maximize_window()

# Get the initial scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(5) #TODO: Replace for explicit waits
    # Calculate new scroll height and compare it with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # if the new and last height are equal, it means that there isn't any new page to load, so we stop scrolling
        break
    else:
        last_height = new_height
driver.quit()


