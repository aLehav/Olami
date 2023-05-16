import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Base URL for the UCSD newspaper archives
base_url = "https://library.ucsd.edu/dc/"

# Load the subpage links from the subpage_links.json file
with open("subpage_links.json", "r") as f:
    subpage_links = json.load(f)

# List to store all the PDF links
pdf_links = []

# Loop through all the subpages and scrape the PDF links
for subpage_link in subpage_links:
    # Make a GET request to the subpage URL
    response = requests.get(subpage_link)

    # Create a BeautifulSoup object from the response HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the PDF links on the page
    pdf_links_on_page = soup.find_all('a', class_='dams-search-thumbnail-link') #pdf_links_on_page = soup.find_all('li', class_='dams-sr') 

    # Loop through all the PDF links and extract the PDF URL
    for pdf_link_on_page in pdf_links_on_page:
        try:
            # Extract the relative URL for the PDF
            pdf_url = pdf_link_on_page['href']

            pdf_url = pdf_url.replace("/dc/", "")

            # Construct the absolute URL for the PDF file and add the "_1.pdf" suffix
            date_url = f"{base_url}{pdf_url.split('?')[0]}"
            print(date_url)
            date_response = requests.get(date_url)
            date_soup = BeautifulSoup(date_response.content, 'html.parser')

            # Find the date element
            date_elem = date_soup.find('dt', string='Creation Date').find_next_sibling('dd').find('ul', class_='unstyled').find('li').get_text(strip=True)
            if date_elem:
                date = date_elem
            else:
                date = None

            # Check if the date element exists and formats the dates (YYYY_mm_dd)
            if date_elem is not None:
                date_obj = datetime.strptime(date_elem, '%B %d, %Y')
                formatted_date = date_obj.strftime('%Y_%m_%d')
                print(formatted_date)
            else:
                raise ValueError("Could not find date element")

        except (KeyError, ValueError, AttributeError) as e:
            # Handle any exceptions that occur
            print(f"Error: {e}")
            continue
    