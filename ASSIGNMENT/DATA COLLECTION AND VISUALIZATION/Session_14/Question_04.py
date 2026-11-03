import pandas as pd

# CSV must contain genre and box_office_collection columns
df = pd.read_csv("bookmyshow_movies.csv")

genre_average = df.groupby("genre")["box_office_collection"].mean()
genre_average = genre_average.sort_values(ascending=False)

print("Average Box Office Collection by Genre:")
print(genre_average)

# Output: Sorted average box office collection for each genre.
