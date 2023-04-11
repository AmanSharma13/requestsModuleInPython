import requests
from bs4 import BeautifulSoup

links = ['https://www.codewithharry.com/blog', 'https://www.codewithharry.com/video', 'https://www.codewithharry.com/contact']

for link in links:
    r = requests.get(link)
    with open(f"html/{link.split('/')[-1]}.html", "w") as f:
        f.write(r.text)