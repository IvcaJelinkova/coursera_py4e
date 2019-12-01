# ex11_regular_expressions.py

import re

# 1) print lines starts with 'From: '
fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if re.search('^From: ', line):
        print(line)

print()


# 2) print list of strings from text:
x = 'My 2 favorite number are 19 and 42. '
y = re.findall('[0-9]+', x)
print('Faforite number:', y)


# 3) search for mail adresses:
x = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:16:14 2008'
y = re.findall('\S+@\S+', x)
print('Mail:', y)





