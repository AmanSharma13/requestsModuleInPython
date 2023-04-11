import requests
from PIL import Image
from io import BytesIO

url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe"

r = requests.get(url)
i = BytesIO(r.content)
fp = open("winrar.exe", "wb")
fp.write(r.content)
fp.close()

