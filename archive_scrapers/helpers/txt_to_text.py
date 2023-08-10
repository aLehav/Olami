from bs4 import BeautifulSoup
import requests


def get_article_text(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    p_tags = soup.find_all('p')
    text = "\n".join([p.get_text() for p in p_tags])

    return text