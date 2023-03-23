# Selecting Elements From Within Ajax Dropdowns 
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select # main package
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
website = "https://www.adamchoi.co.uk/overs/detailed"
path = "C:/Users/harsh/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(path,options=options,service=Service(ChromeDriverManager().install()))
driver.get(website) # scrape the website using the webdriver
# driver.find_element_by_id('id'), driver.find_elements_by_class_name() <- list

dropdown = Select(driver.find_element(By.ID,"country")) #for Ajax dropdowns
# Example: Scrape Spain's football data
spain = dropdown.select_by_visible_text("Spain")
# Create weights (time delay involved in scraping)
# "loading page"
time.sleep(3) # 3 seconds time delay, before code execution

matches = driver.find_elements(By.TAG_NAME,'tr') # list
# XPath indexing starts with 1
# Get each data in different lists
date,home,score,away = [],[],[],[]
for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    curr_home = match.find_element(By.XPATH,'./td[2]').text
    home.append(curr_home)
    # print(curr_home)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away.append(match.find_element(By.XPATH,'./td[4]').text)

# Exporting The Data Into A CSV File
df = pd.DataFrame({"date":date,"home_team":home,"score":home,"away_team":away})
df.to_csv('py4e/Web Scraping/football_data_spain.csv', index=False)
print(df)