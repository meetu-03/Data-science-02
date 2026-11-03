#Create a Python class called Playlist with a private attribute _songs (a list) and a public method add_song(song) to add a song title to the playlist. Print the playlist after adding 3 songs.

class Playlist:

    def __init__(self):
        self._songs = []  # Private attribute

    def add_song(self, song):
        self._songs.append(song)

    def display_playlist(self):
        print("Current Playlist:", self._songs)


# Example Usage:
my_playlist = Playlist()

# Adding 3 songs
my_playlist.add_song("Song A")
my_playlist.add_song("Song B")
my_playlist.add_song("Song C")

# Displaying the playlist
my_playlist.display_playlist()

    




    






    
