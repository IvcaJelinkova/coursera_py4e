# ex08_02_lists.py

some = [1, 9, 21, 10, 16]

print('Is "9" in list "some"?:', 9 in some)        # True

some.sort()
print('Sorted list some:', some)

print('Len of some:', len(some))
print('Max of some:', max(some))
print('Min of some:', min(some))
print('Sum of some:', sum(some))
print('Average of some:', sum(some)/len(some))

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
stuff = abc.split()             # list
print('Metode split "With three words":', stuff)
print('2. element of the sentence:', stuff[1])

for word in stuff:
    print('For cykle:', word)


# days from file:
fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print('3. element of the line started with "From ":', words[2])
