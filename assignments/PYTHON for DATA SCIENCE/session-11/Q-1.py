# Write a recursive function in Python called print_playlist_songs(songs) that takes a list of song names (like a Spotify playlist) and prints each song name one by one using recursion

def print_playlist_songs(songs):
    if len(songs) == 0:
        return

    print(songs[0])
    print_playlist_songs(songs[1:])


songs = ["The Last Ride", "Him", "For A Reason", "Senorita"]

print_playlist_songs(songs)