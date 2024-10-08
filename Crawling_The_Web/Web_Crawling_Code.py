#Simple Web Crawler script using a While Loop

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Defining the web page to crawl through, the specific hyperlink to access(position) and the duration to crawl through these links(count).
url = input('Enter URL - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Usmah.html'
c = input('Enter Count - ')
if len(c) < 1:
    c = 7
p = input('Enter Position - ')
if len(p) < 1:
    p = 18 
count = int(c)
position = int(p)-1

#The Web Crawler While Loop
while count > 0: 
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = count - 1
    url = tags[position].get('href', None)
    print(url)
    

