# Task 5: Download a sample Instagram comments text file (or create your own with at least 10 lines), then write a Python script to extract all valid Instagram usernames (pattern: starts with '@', followed by letters, numbers, underscores, minimum 3 characters) using re.findall() and print the unique usernames.


import re

# 1. Create a dummy comments file for demonstration
comments_data = """ Great photo @alex_123!
Love this @sam_v.
Hey @a_ is too short.
Awesome content @dev_guy99 and @alex_123 again!
Check out @user_test_name for more.
Thanks @photo_guy!
Nice shot @coder_life.
Follow @tech_guru_2026!
Cool @gram_user!
"""

with open("comments.txt", "w") as f:
    f.write(comments_data)

# 2. Extract unique usernames matching pattern (starts with @, min 3 chars of letters, numbers, underscores)
pattern = r'@[a-zA-Z0-9_]{3,}'

with open("comments.txt", "r") as f:
    content = f.read()
    usernames = re.findall(pattern, content)

# Remove duplicates while maintaining clean list
unique_usernames = list(set(usernames))

print("Unique Instagram Usernames Found:")
print(unique_usernames)