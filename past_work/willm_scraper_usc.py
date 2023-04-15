import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the website to scrape
url = "https://dailytrojan.com/2009/06/"
domain = "https://dailytrojan.com"

# Make a request to the website
response = requests.get(url)
html_content = response.content

# Parse the html content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the links on the website
links = soup.find_all("a")

# Store the links to editions in a set to avoid duplicates
edition_links = set()

# Loop through the links and store only the links that are relevant to the 2009 editions
for current_link in links:
    if current_link.has_attr("href") and "200" in current_link["href"]:
        edition_links.add(domain + current_link["href"])

# Create a DataFrame from the list of edition links
edition_links_df = pd.DataFrame(edition_links, columns=["edition_links"])

# Save the DataFrame as a CSV file
edition_links_df.to_csv("daily_trojan_june_2009_links.csv", index=False)

print("Scraping completed successfully! Go Bruins!")
