# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
#     of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
#     a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# result:
# 04 3
# 06 1
# 07 1
# 09 2
# ...


fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhandle = open(fname)


hours = dict()
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        hour = words[5][:2]
        hours[hour] = hours.get(hour, 0) + 1    # have hour and its count in dict()

# sorted by key (hour):
touple_hours = sorted(hours.items())
for hour, count in touple_hours:
    print(hour, count)


# OR:

# list_hours = list()
# for hour, count in hours.items():
#     list_hours.append((hour, count))
# list_hours = sorted(list_hours)
#
# for hour, count in list_hours:
#     print(hour, count)




#sorted by count of hours
#sorted_hours = sorted([(count, hour) for (hour, count) in hours.items()], reverse=True)
#print(sorted_hours)



