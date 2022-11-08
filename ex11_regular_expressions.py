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
print('Favorite number:', y)            # Favorite number: ['2', '19', '42']


# 3) search for mail adresses:
x = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:16:14 2008'
y = re.findall('\S+@\S+', x)            # \S = non-whitespace; + = opakuje znak 1 nebo vícekrát
print('Mail:', y)


# 4) fine-tuning string extracting = search form mail adress in line
# which starts with From "
y = re.findall('^From (\S+@\S+)', x)    # add (); ^ = začátek řádku; ( = indikuje, kde začíná extrakce stringu
print('Mail:', y)


# 5) find host in mail adress:
line = x
y = re.findall('@([^ ]*)', line)        # [^XYZ] = NEshoda jednoho znaku v seznamu; * = opakuje znak 0 nebo vícekrát
print('host:', y)                       # host: ['uct.ac.za']

# OR

line = x
y = re.findall('^From .*@([^ ]*)', line)
print('tuning host:', y)                # tuning host: ['uct.ac.za']


# 6) Spam Confidence:
handle = open('mbox-short.txt')
numlist = list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))         # Maximum: 0.9907



