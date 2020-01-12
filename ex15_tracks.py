# ex15_tracks.py
# to see table: Track	Artist	Album	Genre

import xml.etree.ElementTree as ET
import sqlite3

# connection with dtb music.xml
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# make some fresh tables (Artist, Album, Track) using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist; 
DROP TABLE IF EXISTS Album; 
DROP TABLE IF EXISTS Track; 

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    name    TEXT UNIQUE
); 

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    artist_id   INTEGER,
    title   TEXT UNIQUE
); 

CREATE TABLE Track ( 
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    title   TEXT UNIQUE, 
    album_id    INTEGER, 
    len     INTEGER, year INTEGER, count INTEGER
); 
''')

# input file
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'music.xml'


# music.xml + def lookup(d, key)
# <dict>
# 		<key>207</key>      # <-- key!
# 		<dict>
# 			<key>Track ID</key><integer>207</integer>
# 			<key>Name</key><string>Don't Let the Old Man In</string>
# 			<key>Artist</key><string>Toby Keith</string>
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
            continue
    return None


# parsing my music library and go to child I want (with detail about songs)
stuff = ET.parse(fname)         # xml ET object
all = stuff.findall('dict/dict/dict')       # to find list of all track details
print('Dict count:', len(all))
for entry in all:
    print('\n\nzpracovávám entry')
    if ( lookup(entry, 'Track ID') is None ):
        continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    year = lookup(entry, 'Year')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None:
        continue

    print(name, artist, album, count, year, length)


    # INSERT or IGNORE or REPLACE my tables with data, attention about generation foreign key (id)
    # INSERT OR IGNORE is for new or existing title/name
    # INSERT OR REPLACE if the unique is violated, it turns into UPDATE
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES (?)''', (artist, ))  # IGNORE if it's already there; artist with comma is touple
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]       # foreign key for album table

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track 
        (title, album_id, len, year, count)
        VALUES (?, ?, ?, ?, ?)''', (name, album_id, length, year, count))

    conn.commit()



# later in SQLite: SELECT Track.title as TRACK, Album.title as ALBUM, Artist.name AS ARTIST
# FROM Track JOIN Album JOIN Artist ON Track.album_id = Album.id
# AND Album.artist_id = Artist.id













