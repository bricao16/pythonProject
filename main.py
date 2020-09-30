import requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.com/volleyball/s?k=volleyball'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())