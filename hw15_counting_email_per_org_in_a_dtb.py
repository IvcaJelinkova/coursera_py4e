# hw15_counting_email_per_org_in_a_dtb.py

# This application will read the mailbox data (mbox.txt) and count
# the number of email messages per organization (i.e. domain name
# of the email address) using a database with the following schema
# to maintain the counts.

# ex. of row: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# organizational count is 536

import sqlite3
import re

conn = sqlite3.connect('counting_organizations.sqlite') # connection to the dtb
cur = conn.cursor()     # cursor object from the connection; traverse data from the result set
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

with open (fname) as file:
    for line in file:
        if not line.startswith('From '):
            continue
        pieces = line.split()
        email = pieces[1]
        org_ls = re.findall('@([^ ]*)', email)
        org = org_ls[0]
        cur.execute('''SELECT count FROM Counts WHERE org = ?''', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
        else:
            cur.execute('''UPDATE Counts SET count = count + 1 
                WHERE org = ?''', (org,))
        conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()





