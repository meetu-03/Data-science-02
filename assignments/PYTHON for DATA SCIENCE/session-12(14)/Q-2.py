#Read the playlist.txt file you created and display each song name in uppercase letters using Python.

with open("playlist.txt", "r") as file:
    for song in file:
        print(song.strip().upper())