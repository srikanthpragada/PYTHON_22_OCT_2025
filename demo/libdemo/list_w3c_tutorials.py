
import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, 'html.parser')

links = bs.find_all("a", class_ = "ga-nav")

for link in links:
    title = link['title']
    href = WEBSITE + link['href']

    if 'javascript:' in href:
        continue

    print(title)
    print(href)
    print('-' * 50)
