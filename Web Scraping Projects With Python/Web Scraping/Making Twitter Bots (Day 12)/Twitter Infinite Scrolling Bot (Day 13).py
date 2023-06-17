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

def get_tweet(element):
    try:
        user = element.find_element_by_xpath(".//span[contains(text(), '@')]").text
        text = element.find_element_by_xpath(".//div[@lang]").text
        tweet_data = [user, text]
    except:
        tweet_data = ['user', 'text'] # Dummy text
    return tweet_data

user_data = []
text_data = []
tweet_ids = set() # Why sets? -> avoid duplicate elements due to Twitter's lazy loading approach (selenium might end up locating duplicate elements with the same XPath)

scrolling = True
while scrolling:
    tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']")))
    for tweet in tweets[-15:]: # Retrieve only the last 15 tweets
        # "tweet_id" helps filter duplicate tweets
        tweet_list = get_tweet(tweet)
        tweet_id = "".join(tweet_list) # Concatenate username and the tweet text
        if tweet_id not in tweet_ids:
            tweet_ids.add(tweet_id)
            user_data.append(tweet_list[0])
            text_data.append(" ".join(tweet_list[1].split()))
            print(user_data)
            print(text_data)

    # Get the initial scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(5) #TODO: Replace for explicit waits
        # Calculate new scroll height and compare it with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # If the new and last height are equal, it means that there isn't any new page to load, so we stop scrolling
            scrolling = False # Break outer loop as well
            break
        else:
            last_height = new_height
            break # If this "break" wasn't present, the script would just scroll to the end of the website without scraping the data from each page. Now it scrapes on every iteration

driver.quit()
# Adding collected data to a .csv file
df_tweets = pd.DataFrame({'user': user_data, 'text': text_data})
df_tweets.to_csv('tweets_infinite_scrolling.csv', index=False)
print(df_tweets)



