# you will extract all the numbers in the file and compute the sum of the numbers
import re


fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'regex_sum_326762.txt'

with open(fname, encoding='utf-8') as fhandle:
    list_nums = list()
    for line in fhandle:
        line = line.rstrip()
        words = line.split()
        for word in words:
            num = re.findall('[0-9]+', word)
            if len(num) < 1:
                continue
            list_nums.append(num)
        #print(line, num)

print(list_nums)

count = 0
total = 0
for num in list_nums:
    while True:
        if len(num) > 1:
            #print(num[0])
            count += 1
            total += int(num[0])
            del num[0]
        break
    #print(num[0])
    count += 1
    total += int(num[0])


print(f'There are {count} values with a sum= {total}')


# optional list comprehension after:
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )



