# ex15_counting_email_in_a_dtb.py

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')    # connection to dtb
cur = conn.cursor()         # cursor is like handle; open file and send sql commands to the cursor and have responses from the same cursor

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')  # dictionary

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()   # list, ex: ['From:', 'stephen.marquard@uct.ac.za']
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))  # tuple
    row = cur.fetchone()    # grap first one and give it back to row
    if row is None:         # like GET; creation of new record
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()   # write on disc

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()


