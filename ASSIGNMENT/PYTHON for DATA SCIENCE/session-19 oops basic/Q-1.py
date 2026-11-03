# Task 1
# Question:
# Define a Python class called Song with attributes title, artist, and duration (in seconds). Create an object for your favorite song and print its details.

# Answer:

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

my_song = Song("Bohemian Rhapsody", "Queen", 354)
print(f"Title: {my_song.title}")
print(f"Artist: {my_song.artist}")
print(f"Duration: {my_song.duration} seconds")