import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV must contain the four required Spotify columns
df = pd.read_csv("spotify_songs.csv")

songs = df[["danceability", "energy", "valence", "popularity"]]
sns.pairplot(songs)
plt.show()

# Output: Pairplot showing relationships between the four features.
# Observation: Write one pattern you see in your actual pairplot.
