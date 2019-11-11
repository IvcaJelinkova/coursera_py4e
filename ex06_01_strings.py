# ex06_01_strings.py

# looping through strings:
fruit = 'banana'
for letter in fruit:
    print(letter)


index = 0
while index < len(fruit):
    letter = fruit[index]
    print(str(index) + '. index pro písmeno: ' + str(letter))
    index += 1
