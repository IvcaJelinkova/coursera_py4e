#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent
# the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using
# a maximum loop to find the most prolific committer.

fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhandle = open(fname)

mails = dict()

for line in fhandle:
    line = line.rstrip()
    #print(line)
    if line.startswith('From '):
        words = line.split()
        #print(words[1])
        mail = words[1]
        mails[mail] = mails.get(mail, 0) + 1
#print(mails)

bigword = None
bigcount = None

for mail, count in mails.items():
    if bigword is None or bigcount < 1:
        bigword = mail
        bigcount = count
    elif bigcount < count:
        bigcount = count
        bigword = mail


print(bigword, bigcount)





