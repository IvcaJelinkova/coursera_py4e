# hw12_following_links_in_html.py

# The program will use urllib to read the HTML from the data files below,
# extract the href= values from the anchor tags, scan for a tag that is in
# a particular position relative to the first name in the list, follow that
# link and repeat the process a number of times and report the last name you
# find.

# TEST: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link.
# Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL – ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' # Anayah (4 repeating, 3 position)
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags
tags = soup('a')
user_count = int(input('Enter number of repeating: '))
user_position = int(input('Enter position: '))
position = 0
for count in range(user_count):
    for tag in tags:
        #print('TAG:', tag)
        #print('\tURL:', tag.get('href', None))
        url = tag.get('href', None)
        print('\tContent:', tag.contents[0])
        position += 1
        if position == user_position:
            #print('3. pozice!!! ')
            print(tag.contents[0], url)
            html = urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            print(position, count+1)
            position = 0
            count += 1
            break

print('The name is:', tag.contents[0])


