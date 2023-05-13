
import requests
from bs4 import BeautifulSoup
# import os
# import time

URL = "file:///C:/Users/GAYATHRI%20PS/AppData/Local/Temp/Temp1_feb_2023.zip/feb_2023.html"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')


with open('output.txt', 'w', encoding="utf-8") as f:
    f.write(str(soup.text))


# import requests
# url = "http://127.0.0.1:8000/contacts"
# payload = {}
# headers = {}
# response = requests.request("GET", url, headers=headers, data = payload)
# print(response.json())






