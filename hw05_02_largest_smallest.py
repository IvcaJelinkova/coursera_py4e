# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done'
# is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4
# and match the output below.


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print('Invalid input. Type "done" for quiting. ')
        continue

    if largest is None:
        largest = num
    elif num > largest:
        largest = num
        # print('actual max: ', largest)

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
        # print('actual min: ', smallest)

print("Maximum is:", largest)
print('Minimum is:', smallest)



# what it prints?
tot = 0
for i in [5, 4, 3, 2, 1]:
    tot = tot + 1
    #print(i)
    #print(tot)
print(tot)
