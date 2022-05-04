from bs4 import BeautifulSoup4
import requests
url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)
soup = BeautifulSoup4(req.text, "html.parser")
print(soup.title)