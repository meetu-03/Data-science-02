# Task 4
# Question:
# Create a custom Python module called playlist_utils.py with a function add_song(playlist, song) that adds a song to a list. Import this module in another script and use it to add three songs to a playlist, then print the final playlist.

# Answer:
# File 1: playlist_utils.py


def add_song(playlist, song):
    playlist.append(song)
    return playlist




import playlist_utils

my_playlist = []

# Add three songs
playlist_utils.add_song(my_playlist, "Bohemian Rhapsody")
playlist_utils.add_song(my_playlist, "Hotel California")
playlist_utils.add_song(my_playlist, "Imagine")

print("Final Playlist:")
print(my_playlist)