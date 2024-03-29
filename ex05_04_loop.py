# pr05_04_loop.py

# counting in a loop
count = 0
print('Before counting:', count)
for number in [9, 41, 12, 3, 74, 15]:
    count += 1
    print(str(count) + '. ' + str(number))

print('After counting:', count)
print('\n')



# summing in a loop
sum = 0
print('SUM before:', sum)
for number in [9, 41, 12, 3, 74, 15]:
    sum = sum + number
    print(str(sum) + ' <-- ' + str(number))

print('SUM after:', sum)
print('\n')


# finding the average in a loop
count = 0
sum = 0
print('Count and SUM before:', str(count) + ',', sum)

for number in [9, 41, 12, 3, 74, 15]:
    count += 1
    sum = sum + number
    print(str(count) + '.: SUM', str(sum) + ' <-- number ' + str(number))

print('Count, SUM and average after: ' + str(count) + ', ' + str(sum) + ', ' + str(round(sum / count, 1)))     # rounding is not in example
print('\n')


# filtering in a loop:
print('Before filtering number > 20: ')
for number in [9, 41, 12, 3, 74, 15]:
    if number > 20:
        print('Larger number:', number)

print('After')
print('\n')


# search using a boolean variable:
found = False
print('Before searching number 3: ', found)
for number in [9, 41, 12, 3, 74, 15]:
    if number == 3:
        found = True
        break       # when found is True, do not need to continue searching
    print(str(found) + ', actual number: ' + str(number))

print('After: ', found)
print('\n')


# finding the smallest value:
smallest_so_far = None
print('Before searching the smallest:', smallest_so_far)

for number in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = number
    elif number < smallest_so_far:
        smallest_so_far = number
    print('The smallest so far: ' + str(smallest_so_far) + ', actual number: ' + str(number))

print('After:', smallest_so_far)
print('\n')

