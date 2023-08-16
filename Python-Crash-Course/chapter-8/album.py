def make_album(artist, title):
    album = {'artist': artist, 'title': title}
    return album

album = make_album('Metallica', 'Master of Puppets')
print(album)
album = make_album('Pink Floyd', 'The Wall')
print(album)
album = make_album('Led Zeppelin', 'IV')
print(album)