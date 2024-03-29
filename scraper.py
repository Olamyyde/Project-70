import requests
import random
from bs4 import BeautifulSoup 

def scrapeWikiArticle(url):
    response = requests.get(url=url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Beautiful soup allows you to find an element by the ID tag.
    title = soup.find(id="firstHeading")

    # print(response.status_code)

    # print(title.string)
    # print(title.content)
    print(title.text)


    # Get all the links
    allLinks = soup.find(id="bodyContent").find_all("a")  #Finds all <a> tags within the article
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

        # Use this link to scrape
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org/" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")
