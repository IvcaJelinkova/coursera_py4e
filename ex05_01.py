# ex05_01.py

# program repeatedly reads numbers until user enters "done"
# once "done" is entered, print out the total, count and average of the numbers
# if the user enters anything other than a number, detect their mistake using "try/except" and print
# an error message and skip to the next number

total = 0
count = 0
while True:
    number = input('Enter number: ')
    if number == 'done':
        break
    try:
        number = int(number)
    except:
        print('Invalid input. For quiting enter "done". ')
        continue
    total = total + number
    count += 1

print('ALL DONE. ')
print(total, count, total / count)
