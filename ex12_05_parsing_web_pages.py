# ex12_05_parsing_web_pages.py

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl      # remove unsupported url

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))