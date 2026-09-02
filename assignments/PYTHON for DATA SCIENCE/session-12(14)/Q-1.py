#Create a text file named playlist.txt and write the names of 5 songs you listened to this week, each on a new line using Python's open() function in write mode.


songs = [
    "What...? - Karan Aujla",
    "Winning Speech - Karan Aujla",
    "Softly - Karan Aujla",
    "295 - Sidhu Moose Wala",
    "Insane - AP Dhillon"
]

with open("playlist.txt", "w") as file:
    for song in songs:
        file.write(song + "\n")
        