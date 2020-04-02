def make_album(artist_name, album_title, no_of_songs=None):
    albums = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }

    if no_of_songs:
        albums['songs'] = no_of_songs

    return albums


print(f"type quit at any time to quit")

while True:
    artist_name = input("Please enter an artist name: ")

    if artist_name == 'quit':
        break

    album_title = input("Please eneter an album title: ")

    if album_title  == 'quit':
        break

    album = make_album(artist_name, album_title)
    print(album)
print("\nThanks for responding!")