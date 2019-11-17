# ex07_02_files.py

fhandle = open('mbox.txt')
count = 0
for line in fhandle:
    count += 1
print('Line Count =', count)
