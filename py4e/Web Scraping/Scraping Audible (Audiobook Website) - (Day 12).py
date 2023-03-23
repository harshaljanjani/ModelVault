# Scraping Data From Amazon's Audible (Audiobook Website)
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options # Headless Mode
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
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


container = driver.find_element(By.CLASS_NAME,'adbl-impression-container ') # get all audiobooks 
products = container.find_elements(By.CLASS_NAME, 'productListItem') # get immediate children which are <li> tags *(list dtype)
# representative attributes -> runtimeLabel, authorLabel
# multiple classes -> use .contains()
book_author = []
book_title = []
book_length = []
for product in products:
    title = product.find_element(By.XPATH,".//h3[contains(@class,'bc-heading')]").text
    author = product.find_element(By.XPATH,".//li[contains(@class,'authorLabel')]").text
    runtime = product.find_element(By.XPATH,".//li[contains(@class,'runtimeLabel')]").text
    book_title.append(title);
    book_author.append(author);
    book_length.append(runtime);

driver.quit()
df = pd.DataFrame({"Book Title":book_title,"Book Author":book_author,"Book Runtime":book_length})
df.to_csv('py4e/Web Scraping/audible_books_data_headless.csv', index=False)
print(df)