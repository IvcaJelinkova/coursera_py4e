# hw15_many_to_many_dtb.py

# This application will read roster data in JSON format,
# parse the file, and then produce an SQLite database
# that contains a User, Course, and Member table
# and populate the tables from the data file.

# data:
# [
#   [
#     "Mabel",
#     "si110",
#     1
#   ],

import sqlite3
import json

# connection with dtb:
conn = sqlite3.connect('dtbroster.sqlite')
cur = conn.cursor()

# creating tables:
cur.executescript('''
    DROP TABLE IF EXISTS User; 
    DROP TABLE IF EXISTS Course; 
    DROP TABLE IF EXISTS Member;
    
    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
        name TEXT UNIQUE
    ); 
    
    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
        title TEXT UNIQUE
    ); 
    
    CREATE TABLE Member (
        user_id INTEGER, 
        course_id INTEGER, 
        role INTEGER, 
        PRIMARY KEY (user_id, course_id)
    )
''')

# loading the file with data:
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# data preparation & giving data to sql:
with open(fname) as file:
    str_data = file.read()
    json_data = json.loads(str_data)
    for data in json_data:
        name = data[0]
        title = data[1]
        role = data[2]
        print(name, title, role)

        # giving data to sql:
        cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name, ))
        cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
        user_id = cur.fetchone()[0]

        cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title, ))
        cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
        course_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
                    VALUES (?, ?, ?)''', (user_id, course_id, role, )) # if there is the same combination of user_id and course_id (primary key) - it will update the data

        conn.commit()

# later in sqlite:
# SELECT hex(User.name || Course.title || Member.role ) AS X FROM
#     User JOIN Member JOIN Course
#     ON User.id = Member.user_id AND Member.course_id = Course.id
#     ORDER BY X

