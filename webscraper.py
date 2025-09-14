import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string if soup.title else 'No title found'
    except:
        print("Some error occurred while trying to scrape the website.")
        return None

url = input("Enter the URL of the website to scrape: ")
title = scrape_website(url)
if title:
    with open('webscraper.txt','a') as f:
        f.write(title + '\n')
    print("Website Title:", title)
else:
    print("Failed to retrieve the website title.")    