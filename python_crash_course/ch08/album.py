def make_album(artist_name, album_title, no_of_songs=None):

    albums = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }

    if no_of_songs:
        albums['songs'] = no_of_songs

    return albums


album = make_album('george ezra', 'budapest')
print(album)
album = make_album('coldplay', 'parachuts', 20)
print(album)
album = make_album('bon jovi', 'crosswords')
print(album)
