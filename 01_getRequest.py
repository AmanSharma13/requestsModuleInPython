import requests

r = requests.get("https://www.codewithharry.com")

with open("index.html", "w") as f:
    f.write(r.text)