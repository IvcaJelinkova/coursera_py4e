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
for line in fhandle:
    if line.startswith('line'):
        print(line)                 # print printing new line also
