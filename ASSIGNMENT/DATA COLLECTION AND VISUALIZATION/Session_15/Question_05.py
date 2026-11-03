import pandas as pd
from ydata_profiling import ProfileReport

# Keep swiggy_orders.csv in this folder
df = pd.read_csv("swiggy_orders.csv")

report = ProfileReport(df, title="Swiggy Orders Report")
report.to_file("swiggy_report.html")

print("Report created: swiggy_report.html")

# Output: HTML report containing statistics, missing values and data types.
