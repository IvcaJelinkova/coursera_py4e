# ex09_dictionaries.py

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)

print('fred' in jjj)        # --> True

# simplified counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


# two iteration
for name, number in counts.items():
    print(name, number)


#  bigword + counts
name = input('Enter file: ')
fhandle = open(name)

counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

# get()
stuff = dict()
print(stuff.get('candy',-1))


# worked_exercise:
di = dict()
handle = open(name)
for line in handle:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        print(word)
        if word in di:
            di[word] = di[word] + 1
            print('**Existing**')
        else:
            di[word] = 1
            print('**NEW**')
        print(di[word])

print(di)

