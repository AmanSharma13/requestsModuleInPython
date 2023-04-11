import os
from bs4 import BeautifulSoup


for file in os.listdir("html"):
    # print(file)
    with open(f"html/{file}") as f:
        htmlContent = f.read()
        soup = BeautifulSoup(htmlContent, "html.parser")
        for link in soup.find_all("a"):
            print(link.get("href"))
