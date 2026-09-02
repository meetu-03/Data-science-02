#Write a generator function called playlist_generator that takes a list of song names and yields each song one at a time, simulating a Spotify playlist shuffle.
def playlist_generator(songs):
    for song in songs:
        yield song


songs = ["Perfect", "Believer", "Shape of You", "Blinding Lights", "Hawayein"]

playlist = playlist_generator(songs)

for song in playlist:
    print(song)