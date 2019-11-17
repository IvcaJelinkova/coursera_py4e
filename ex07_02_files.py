# ex07_02_files.py

fhandle = open('m_box.txt')
# count = 0
# for line in fhandle:
#     count += 1
# print('Line Count =', count)

# 2) reading the "whole" file:
# inp = fhandle.read()
# print(inp)
# print(len(inp))
# print(inp[:10])

# 3) searching through a file:
# for line in fhandle:
#     line = line.rstrip()
#     #if line.startswith('line'):
#     #    print(line)                 # print printing new line also
#
#     #or:                            # stylish thing
#     if not line.startswith('line'):
#         continue
#     print(line)


# 4) using "in" to select lines:
# for line in fhandle:
#     line = line.rstrip()
#     if not 'line' in line:
#         continue
#     print(line)


# 5) bad file names from user:
fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

print('File is open. :-)')
