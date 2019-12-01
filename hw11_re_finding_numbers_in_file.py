# you will extract all the numbers in the file and compute the sum of the numbers
import re


fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'regex_sum_42.txt'

fhandle = open(fname)
list_nums = list()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        num = re.findall('[0-9]+', word)
        if len(num) < 1:
            continue
        #num = int(num[0])
        #print(num)
        list_nums.append(num)
    print(line, num)

print(list_nums)

count = 0
sum = 0
for num in list_nums:
    while True:
        if len(num) > 1:
            print(num[0])
            count += 1
            sum += int(num[0])
            del num[0]
        break
    print(num[0])
    count += 1
    sum += int(num[0])


print(f'There are {count} values with a sum= {sum}')



