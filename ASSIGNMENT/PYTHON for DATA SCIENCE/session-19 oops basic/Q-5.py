# Task 5
# Question:
# Refactor your Song class so that the duration attribute is optional in the constructor (default to 0 if not provided).
# Hint: Use a default argument for duration in the __init__() method.

# Answer:


class Song:
    # Set default value for duration to 0
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

# Creating an object with the duration provided
song1 = Song("Bohemian Rhapsody", "Queen", 354)
print(f"Song 1 - Title: {song1.title}, Duration: {song1.duration}")

# Creating an object without providing the duration
song2 = Song("Mystery Track", "Unknown Artist")
print(f"Song 2 - Title: {song2.title}, Duration: {song2.duration}")