import pandas as pd
from ydata_profiling import ProfileReport

# Keep spotify_top_100.csv in this folder
df = pd.read_csv("spotify_top_100.csv")

report = ProfileReport(df, title="Spotify Top 100 Songs Report")
report.to_file("spotify_report.html")

print("Report created: spotify_report.html")

# Output: HTML report with statistics, missing values and data types.
