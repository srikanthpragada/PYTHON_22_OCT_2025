import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.tiobe.com/tiobe-index"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, 'html.parser')

table = bs.find(id ="top20")
tbody = table.find("tbody")
rows = tbody.find_all("tr")
for row in rows[:10]:
    cols = row.find_all('td')
    name = cols[4].text
    rank = cols[5].text
    print(f"{name:20} {rank}")



