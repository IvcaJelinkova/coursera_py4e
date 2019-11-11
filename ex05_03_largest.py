# pr05_03_largest.py

# finding the largest value:

largest_so_far = -1
print('Before the largest:', largest_so_far)

for number in [9, 41, 12, 3, 74, 15]:
    if number > largest_so_far:
        largest_so_far = number
    print('Actual the largest: ' + str(largest_so_far) + ', actual number: ' + str(number))

print('After:', largest_so_far)