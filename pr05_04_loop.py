# pr05_04_loop.py

# counting in a loop

count = 0
print('Before:', count)
for number in [9, 41, 12, 3, 74, 15]:
    count += 1
    print(str(count) + '. ' + str(number))

print('After:', count)
print('\n')



# summing in a loop

sum = 0
print('SUM before:', sum)
for number in [9, 41, 12, 3, 74, 15]:
    sum = sum + number
    print(str(sum) + ' <-- ' + str(number))

print('SUM after:', sum)
