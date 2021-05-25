import requests
from bs4 import BeautifulSoup

URL = "https://gomovies-online.cam/all-films-2"
headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
for link in soup.find_all('img'):
	link = link.get('data-src')
	if link:
		if link[:44] == "https://static.gomovies-online.cam/dist/img/":
			print(link)
