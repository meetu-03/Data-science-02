# Task 2
# Question:
# Add a method play_preview(self) to the Song class that prints 'Playing 30-second preview of [title] by [artist]'. Call this method using the object you created.

# Answer:


class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")

my_song = Song("Bohemian Rhapsody", "Queen", 354)
my_song.play_preview()