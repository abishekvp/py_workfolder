
import requests
from bs4 import BeautifulSoup
import os
import time

URL = "https://rittransport.com/may02.php"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
with open('out.txt', 'w', encoding="utf-8") as f:
    for i in soup:
        i=str(i)
        print(i)
        f.write(i)

sno=[]
rno=[]
route=[]
bptb=[]
bpt=[]

file=open('out.txt', 'r').readlines()

for i in file:
    print(i)
    if 'class="sno"'in i:
        sno.append(str(BeautifulSoup(i).text).strip())
    elif '<td class="rno" colspan="1">' in i:
        if 'font' in i:
            continue
        else:
            rno.append(str(BeautifulSoup(i).text).strip())
    elif '<td class="bptb"' in i:
        bptb.append(str(BeautifulSoup(i).text).strip())
    elif 'class="bpt"' in i:
        i = str(BeautifulSoup(i).text).strip()
        for j in i:
            if j.isnumeric() or i=='.':
                print(i)
                print(j)
        time.sleep(3)

bptdata=[]

inp=int(input())
l=[]
for i in range(inp+1):
    v=0
    for j in range(i):
        v+=j
    l.append(v)
    if inp in l:
        print(True)
        break
else:print(False)
     

print(sno, '\n\n', rno, '\n\n', bptb, '\n\n', bpt)


# import re
# import urllib.request
# response = urllib.request.urlopen('https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_dynamic_websites.html')
# # html = response.read()
# # text = html.decode()
# # print(re.findall('(.*?)',text))

# print(response)

