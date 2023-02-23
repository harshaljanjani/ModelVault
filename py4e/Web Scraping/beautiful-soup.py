# Beautiful-Soup For Web-Scraping
from bs4 import BeautifulSoup
import requests
website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website) # get response object
content = response.text
soup = BeautifulSoup(content,"lxml") # lxml parser
# print(soup.prettify()) # gets entire HTML code of the website
box = soup.find('article',class_='main-article')
title = box.find('h1').get_text() # exclude anything outside the 'box'
# print(title)
# Without get_text(), it returns the HTML for the transcript
transcript = box.find('div',class_='full-script').get_text(strip=True,separator=' ')
# print(transcript)

# Export the data into a .txt file
# Without encoding="utf-8" -> charcodec error
with open(f'{title}.txt','w',encoding="utf-8") as file:
    file.write(transcript)


# Task 1: Get The Transcripts Of All The Movies Listed On The Homepage Using Nested Web-Scraping
# Solved:
# Scraping multiple pages
root = 'https://subslikescript.com/'
website = f'{root}movies'
response = requests.get(website)
content = response.text
soup = BeautifulSoup(content,"lxml") # lxml parser
box = soup.find('article',class_='main-article')
movies = box.find_all("a",href=True) # all href's are also collected in movies 'list'
links = []
for movie in movies:
    links.append(root+movie['href']) # root URL + movie-link endpoints
print(links)

# Get transcript of each of the links
for link in links:
    website = link
    response = requests.get(website)
    content = response.text
    soup = BeautifulSoup(content,"lxml") # lxml parser
    box = soup.find('article',class_='main-article')
    title = box.find('h1').get_text() # exclude anything outside the 'box'
    # print(title)
    # Without get_text(), it returns the HTML for the transcript
    transcript = box.find('div',class_='full-script').get_text(strip=True,separator=' ')
    with open(f'{title}.txt','w',encoding="utf-8") as file:
        file.write(transcript) # individual transcript files saved for each movie

# Task 2: Implement a Selenium/Scrapy-like Pagination Measure In BeautifulSoup
root = 'https://subslikescript.com/'
website = f'{root}movies_letter-A'
response = requests.get(website)
content = response.text
soup = BeautifulSoup(content,"lxml")
pagination = soup.find("ul",class_='pagination')
pages = pagination.find_all('li',class_='page-item')
last_page = pages[-2].text #last item in the li is an 'arrow'
links = []
for page in range(1,3): # 1 to 92 Pages -> 1,int(last_page)+1
    website = f'{root}movies_letter-A?page={page}'
    response = requests.get(website)
    content = response.text
    # new soup
    soup = BeautifulSoup(content,"lxml")
    box = soup.find('article',class_='main-article')
    movies = box.find_all("a",href=True) # all href's are also collected in movies 'list'
    for movie in movies:
        links.append(root+movie['href']) # root URL + movie-link endpoints
    print(links)
    # Get transcript of each of the links
    for link in links:
        try:
            website = link
            response = requests.get(website)
            content = response.text
            soup = BeautifulSoup(content,"lxml") # lxml parser
            box = soup.find('article',class_='main-article')
            title = box.find('h1').get_text() # exclude anything outside the 'box'
            # print(title)
            # Without get_text(), it returns the HTML for the transcript
            transcript = box.find('div',class_='full-script').get_text(strip=True,separator=' ')
            with open(f'{title}.txt','w',encoding="utf-8") as file:
                file.write(transcript) # individual transcript files saved for each movie
        except:
            print("Invalid File Name")
        