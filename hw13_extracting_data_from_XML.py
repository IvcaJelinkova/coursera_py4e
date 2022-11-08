# hw13_extracting_data_from_XML.py

# The program will prompt for a URL, read the XML data from that URL using urllib and then parse
# and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# ex:
    # <commentinfo>
        # <note>This file contains the sample data for testing</note>
        # <comments>
            # <comment>
                # <name>Romina</name>
                # <count>97</count>
            # </comment>
            # <comment>
                # <name>Laurie</name>
                # <count>97</count>
            # </comment>

from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# url = input('Enter URL – ')
# if len(url) < 1:
#     url = 'http://py4e-data.dr-chuck.net/comments_42.xml'   # count: 50, sum: 2553
# data = urlopen(url, context=ctx).read()

data = '''
<commentinfo>
    <note>This file contains the sample data for testing</note>
    <comments>
        <comment>
            <name>Romina</name>
            <count>97</count>
        </comment>
        <comment>
            <name>Laurie</name>
            <count>97</count>
        </comment>
'''

tree = ET.fromstring(data)
print(tree)
lst = tree.findall('comments/comment')
print('Count:', len(lst))
sum = 0
for item in lst:
    #print('Count:', item.find('count').text)
    num = int(item.find('count').text)
    sum = sum + num
print(sum)





