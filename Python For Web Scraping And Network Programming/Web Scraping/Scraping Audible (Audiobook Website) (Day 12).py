# Scraping Data From Amazon's Audible (Audiobook Website)
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options # Headless Mode
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# for explicit waits
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--headless") # set headless = 'True'
options.add_argument('window-size=1920x1080')

website = "https://www.audible.com/search?ipRedirectOverride=true&ipRedirectOverride=true&overrideBaseCountry=true&overrideBaseCountry=true&pf_rd_p=ba485dc1-f49f-438a-92e0-9e8cdea09e44&pf_rd_r=Y1JJ6FRJMT2K62JC6QKD&pageLoadId=vapa6Z73ovbWQU3X&creativeId=a2d315be-e6e7-4f3c-849a-e47e680dcd54"
path = "C:/Users/harsh/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(path,options=options,service=Service(ChromeDriverManager().install()))
driver.get(website)
driver.maximize_window()

# handling pagination
pagination = driver.find_element(By.XPATH,"//ul[contains(@class,'pagingElement')]")
pages = pagination.find_elements(By.TAG_NAME,'li')
last_page = 10 # FOR ALL PAGES: int(pages[-2].text) # just before the 'right arrow' # value: 60; for demonstrative purposes, only scraping the first 10 pages

book_author = []
book_title = []
book_length = []
curr_page = 1;
while curr_page <= last_page:
    # time.sleep(2) -> added explicit waits instead
    container = WebDriverWait(driver,5).until(EC.presence_of_element_located(By.CLASS_NAME,'adbl-impression-container ')) # get all audiobooks 
    products = WebDriverWait(container,5).until(EC.presence_of_element_located(By.CLASS_NAME,'productListItem')) # get immediate children which are <li> tags *(list dtype)
    # representative attributes found -> runtimeLabel, authorLabel, bc-heading
    # multiple classes -> use .contains()
    for product in products:
        title = product.find_element(By.XPATH,".//h3[contains(@class,'bc-heading')]").text
        author = product.find_element(By.XPATH,".//li[contains(@class,'authorLabel')]").text
        runtime = product.find_element(By.XPATH,".//li[contains(@class,'runtimeLabel')]").text
        book_title.append(title);
        book_author.append(author);
        book_length.append(runtime);
    # navigate to next page
    curr_page += 1
    try:
        next_page = driver.find_element(By.XPATH,"//span[contains(@class,'nextButton')]")
        next_page.click()
    except:
        pass

driver.quit()
df = pd.DataFrame({"Book Title":book_title,"Book Author":book_author,"Book Runtime":book_length})
df.to_csv('py4e/Web Scraping/audible_books_with_pagination.csv', index=False)
print(df)