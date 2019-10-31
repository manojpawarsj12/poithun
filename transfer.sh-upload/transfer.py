import requests
import os
from os import path
url = "https://transfer.sh/"
file = input(r"enter a directory of file ")
if path.exists(file):
    pass
elif os.path.getsize(file) < 1073741824:
    print("file size is greater than 1GB try again bruhh")
    exit(0)
else:
    print("wrong file path try again \n")
    exit(0)
file = {'{}'.format(file): open(file, 'rb')}
response = requests.post(url, files=file)
download_link = response.content.decode('utf-8')
print("Link to download file ", download_link)
