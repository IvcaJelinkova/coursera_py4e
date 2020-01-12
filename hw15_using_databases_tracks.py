# hw15_using_databases_tracks.py

# This application will read an iTunes export file in XML and produce
# a properly normalized database with given structure


import xml.etree.ElementTree as ET
import sqlite3

# connection with db
conn = sqlite3.connect('dbtracks_teacher.sqlite')
cur = conn.cursor()


# making tables
cur.executescript('''
DROP TABLE IF EXISTS Artist; 
DROP TABLE IF EXISTS Genre; 
DROP TABLE IF EXISTS Album; 
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


# opening file with tracks
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'Library.xml'

# <dict>
# 	<key>Major Version</key><integer>1</integer>
# 	<dict>
# 		<key>207</key>
# 		<dict>
# 			<key>Track ID</key><integer>207</integer>
# 			<key>Name</key><string>Don't Let the Old Man In</string>
# 			<key>Artist</key><string>Toby Keith</string>
#			<key>Album</key><string>Don't Let the Old Man In</string>
#			<key>Genre</key><string>Rock</string>
#			<key>Total Time</key><integer>173061</integer>
#			<key>Rating</key><integer>100</integer>
#           <key>Play Count</key><integer>16</integer>

def lookup(dict_track, key):
    '''look up the child in dictionary f. ex. the name of album'''
    found = False
    for child in dict_track:
        if found == True:
            key = child.text
            #print(f'\tKey je teď:', key)
            return key
        if child.tag == 'key' and child.text == key:
            found = True
            #print('teď jsem našla')
    return None


stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Number of tracks:', len(all), '\n')

for entry in all:
    #print('\n\nZpracovávám entry: ')
    track = lookup(entry, 'Name')
    print('name je:', track)
    genre = lookup(entry, 'Genre')
    print('Genre je:', genre)
    artist = lookup(entry, 'Artist')
    print('Artist:', artist)
    album = lookup(entry, 'Album')
    print('Album:', album)
    length = lookup(entry, 'Total Time')
    print('total time:', length)
    rating = lookup(entry, 'Rating')
    print('rating:', rating)
    count = lookup(entry, 'Play Count')

    if track is None or artist is None or album is None or genre is None:
        continue

    print(track, genre, artist, album, length, rating, count, '\n\n')


    # filling the table:
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES (?)''', (artist, ))
    cur.execute('''SELECT id FROM Artist WHERE name = ?''', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES (?)''', (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (artist_id, title)
        VALUES (?, ?)''', (artist_id, album))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''', (track, album_id, genre_id, length, rating, count))


    conn.commit()

# later in SQLite
# -- table: track, artist, album, genre
#
# SELECT Track.title as Track, Artist.name as Artist, Album.title as Album, Genre.name as Genre
# FROM Track JOIN Artist JOIN Album JOIN Genre
# ON Album.artist_id = Artist.id and Track.album_id = Album.id and Track.genre_id = Genre.id;
