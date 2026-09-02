#Task 4: Create a custom Python module called playlist_utils.py with a function add_song(playlist, song) that adds a song to a list. Import this module in another script and use it to add three songs to a playlist, then print the final playlist.

def add_song(playlist, song):
    playlist.append(song)
    return playlist




import playlist_utils

my_playlist = []

playlist_utils.add_song(my_playlist, "Song A")
playlist_utils.add_song(my_playlist, "Song B")
playlist_utils.add_song(my_playlist, "Song C")

print("Final Playlist:", my_playlist)