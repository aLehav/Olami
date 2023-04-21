import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_pdf_links(pdf_full_url):
    """
    Retrieves all PDF links from a given URL

    Args:
        url (str): The URL to retrieve PDF links from

    Returns:
        A list of PDF links (str)
    """
    # Retrieve HTML content from URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links in the HTML content
    links = soup.find_all('a')

    # Retrieve all links that contain ".pdf"
    pdf_links = [link['href'] for link in links if '.pdf' in link.get('href', '')]

    # Return the PDF links
    return pdf_links

def find_pdf_date(pdf_links):
    pdf_dates = {}
    for pdf_link in pdf_links:
        pdf_url = pdf_link.get('href')
        if pdf_url.endswith('/_1.pdf'):
            date_url = pdf_url[:-7] # Remove the "/_1.pdf" suffix to get the date URL
            date_request = requests.get(date_url)
            date_soup = BeautifulSoup(date_request.text, 'html.parser')
            try:
                date_str = date_soup.find('div', class_='vc_tta-panel-body').find('strong').text.strip()
                date_obj = datetime.strptime(date_str, '%B %d, %Y')
                date_formatted = date_obj.strftime('%Y_%m_%d')
                pdf_dates[pdf_url] = date_formatted
            except ValueError:
                print(f"Date format for {pdf_url} is unexpected, skipping...")
    return pdf_dates


