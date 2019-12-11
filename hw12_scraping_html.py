# hw12_scraping_html.py
# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum of the numbers
# in the file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'  # sum = 2553, count = 50
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
count = 0
total = 0
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    #print('Number:', tag.get('class', None))
    print('Comments:', tag.contents[0])
    num = int(tag.contents[0])
    #print('Attrs:', tag.attrs)
    count += 1
    total += int(tag.contents[0])
    print(f'actual count: {count} and actual total: {total}')
print(count)
print(total)


