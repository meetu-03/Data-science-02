#Task 2: Write a script that uses the os module to create a new folder named 'MyDownloads' in your current working directory, then print the absolute path of the new folder.

import os

# Create folder if it doesn't already exist
folder_name = 'MyDownloads'
os.makedirs(folder_name, exist_ok=True)

# Get and print absolute path
abs_path = os.path.abspath(folder_name)
print("Absolute path:", abs_path)