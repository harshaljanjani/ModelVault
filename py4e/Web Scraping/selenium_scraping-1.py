# for websites running on JavaScript
# XPath syntax - '//tag[@AttributeName="Value"]'
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Click On A Button
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
website = "https://www.adamchoi.co.uk/overs/detailed"
path = "C:/Users/harsh/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(path,options=options,service=Service(ChromeDriverManager().install()))
driver.get(website) # scrape the website using the webdriver
# driver.find_element_by_id('id'), driver.find_elements_by_class_name() <- list
all_matches_button = driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches_button.click()

# Extracting Data From Tables
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
df.to_csv('py4e/Web Scraping/football_data.csv', index=False)
print(df)