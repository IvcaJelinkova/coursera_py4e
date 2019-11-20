# ex08_02_lists.py

some = [1, 9, 21, 10, 16]

print(9 in some)        # True

some.sort()
print(some)

print(len(some))
print(max(some))
print(min(some))
print(sum(some))
print(sum(some)/len(some))

# average:                      disadventage: too much memory when I have lots of numbers!! :-(
numlist = list()
while True:
    number = input('Enter a number (or "done" for quit): ')
    if number == 'done':
        break
    value = float(number)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)


# strings and lists
abc = 'With three words'
stuff = abc.split()     # list
print(stuff)
print(stuff[1])

for word in stuff:
    print(word)


# days from file:
fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])
