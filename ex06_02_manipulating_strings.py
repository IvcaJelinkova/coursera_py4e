# ex06_02_manipulating_strings.py

# using "in" as a logical operator
fruit = 'BANANA'
'n' in fruit        # --> True

if 'A' in fruit:
    print('Found it!')      # when if is True --> Found it!

# A < a
print(fruit.capitalize())
print(fruit.center(25, 'b'))    # vysadí 25-6 béček a doprostřed vsadí BANANA
print(fruit.endswith('NA'))     # True/False if str ends with 'NA'
print(fruit.find('A'))          # return index of the first position char 'A'
print(fruit.lstrip('B'))        # remove 'B' from left
print(fruit.replace('NA', 'NO', 1))     # replace 'NO' insted of 'NA' in the first place
print(fruit.strip('BA'))        # --> NAN




