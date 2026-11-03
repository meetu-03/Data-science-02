import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a list of 40 Spotify song genres
genres = [
    "Pop", "Rock", "Hip-Hop", "Jazz", "Pop",
    "Rock", "Classical", "Pop", "Jazz", "Hip-Hop",
    "Rock", "Pop", "Classical", "Jazz", "Pop",
    "Rock", "Hip-Hop", "Pop", "Jazz", "Classical",
    "Rock", "Pop", "Hip-Hop", "Jazz", "Pop",
    "Rock", "Classical", "Pop", "Jazz", "Hip-Hop",
    "Rock", "Pop", "Classical", "Jazz", "Pop",
    "Rock", "Hip-Hop", "Pop", "Jazz", "Classical"
]

df = pd.DataFrame({"Genre": genres})
sns.countplot(data=df, x="Genre", color="green")

plt.title("Number of Spotify Songs by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Songs")
plt.show()

# Output: Countplot showing the number of songs in each genre.
