# #Task 2
# Question:
# Write a script that uses the os module to create a new folder named 'MyDownloads' in your current working directory, then print the absolute path of the new folder.

# Answer:

# Python
import os

folder_name = "MyDownloads"

# Create folder if it doesn't already exist
os.makedirs(folder_name, exist_ok=True)

# Get and print the absolute path
abs_path = os.path.abspath(folder_name)
print(f"Absolute path: {abs_path}")