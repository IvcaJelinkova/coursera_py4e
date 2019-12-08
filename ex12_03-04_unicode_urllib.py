# ex12_03_unicode_characters_and_strings.py

# 256 number in 8 bits of memory
# UTF-8 is recommended practice for encoding
# python program in unicode
# bytes.decode
# str.encode

import urllib.request, urllib.parse, urllib.error

print(ord('H'))     # 72
print(ord('\n'))    # 10


# dict of words frequencies
fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

