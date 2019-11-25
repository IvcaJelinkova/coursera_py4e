# ex10_tuples.py

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)         # dict_items([('csev', 2), ('cwen', 4)])

# sort by values instead of key:
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)              # list of tuples

tmp = sorted(tmp, reverse=True)
print(tmp)


# top 10 most common words:
fhandle = open('romeo.txt')
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

list_counts = list()
for word, count in counts.items():
    new_tuple = (count, word)
    list_counts.append(new_tuple)

list_counts = sorted(list_counts, reverse=True)

for count, word in list_counts[:10]:
    print(word, count)






