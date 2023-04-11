import requests
from tqdm import tqdm
import math
from io import BytesIO

url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe"
r = requests.get(url, stream=True)
totalExpectedBytes = r.headers["Content-Length"]
print(totalExpectedBytes)
bytesReceived = 0
progress_bar  = tqdm(totalExpectedBytes , unit='iB', unit_scale=True)
with open("winrar.exe", 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        f.write(chunk)
        bytesReceived += 128
        progress_bar.update(128)
        # percent = (bytesReceived/int(totalExpectedBytes))*100
        # print(f"\t{bytesReceived}/{totalExpectedBytes}")
        # print(percent.__trunc__())