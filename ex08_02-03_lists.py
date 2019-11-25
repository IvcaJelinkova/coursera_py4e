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


# PyLadies: list in list
znamky = [1, 4, 3, [1, 2, 4], 5, 1]
print(znamky[3][1])     # how to get the second value in nested list




for cislo_radku in range(5):
    for cislo_sloupce in range(5):
        print(cislo_radku * cislo_sloupce, end='\t')
    print()

cislo_radku = 1



tabulka = []
for cislo_radku in range(5):
    radek = []
    for cislo_sloupce in range(5):
        radek.append(cislo_radku * cislo_sloupce)
    tabulka.append(radek)

print(tabulka[2][4])    # číslo řádku, číslo sloupce

del radek

# tabulka je seznam řádků
# řádek je seznam čísel
# tabulka je seznam seznamu čísel :-)

for radek in tabulka:
    for cislo in radek:
        print(cislo, end='\t')
    print()



# seznam seznamů:
pole = [['. '] * 5]




