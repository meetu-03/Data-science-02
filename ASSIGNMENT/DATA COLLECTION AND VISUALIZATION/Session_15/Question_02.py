import pandas as pd
import sweetviz as sv

# Keep both CSV files in this folder
mumbai = pd.read_csv("zomato_mumbai.csv")
delhi = pd.read_csv("zomato_delhi.csv")

report = sv.compare([mumbai, "Mumbai"], [delhi, "Delhi"])
report.show_html("zomato_comparison.html")

print("Report created: zomato_comparison.html")

# Output: HTML comparison report for Mumbai and Delhi restaurants.
