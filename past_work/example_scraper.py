import pandas as pd
import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

url = "https://pickupline.net/tv-show-movie-themed-pick-up-lines/"

# send a request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# find all the links with the specified class
links = soup.find_all('a', class_="_self pt-cv-href-thumbnail pt-cv-thumb-default")

added_links = []
# loop through all the links and print the URLs of the child pages
for link in links:
    # check if the link is a child link (i.e., starts with 'https://pickupline.net/')
    if link.has_attr('href'):
        added_links.append(link['href'])

added_links_df = pd.DataFrame(added_links, columns=["Links"])
added_links_df.to_csv('example_scraper_output.csv', index=False)