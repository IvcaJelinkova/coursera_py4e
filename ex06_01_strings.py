# ex06_01_strings.py

# looping through strings:
fruit = 'banana'
for letter in fruit:
    print(letter)

print()


# metoda 2 (not so nice/clever):
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(str(index) + '. index pro písmeno: ' + str(letter))
    index += 1

print()


# looping and counting:
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1

print('Počet výskytů písmene "a": ' + str(count))
