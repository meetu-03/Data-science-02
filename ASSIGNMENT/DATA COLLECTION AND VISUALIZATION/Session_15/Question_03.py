import pandas as pd
import dtale

# Keep myntra_products.csv in this folder
df = pd.read_csv("myntra_products.csv")

d = dtale.show(df)
d.open_browser()

# Output: D-Tale opens in a browser.
# Filter the price column to show prices above 2000.
# Count the filtered products and take a screenshot for submission.
