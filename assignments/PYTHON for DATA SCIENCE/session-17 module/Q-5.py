# Task 5
# Question:
# Set up a new virtual environment using venv, activate it, and install the 'requests' package using pip. Write a short script that imports requests and prints the version installed.
# Hint: Use python -m venv venv_folder, then pip install requests.

# Answer:

# Step 1: Terminal Commands
#
# On Windows (Command Prompt / PowerShell):
# python -m venv venv_folder
# venv_folder\Scripts\activate
# pip install requests
#
# On macOS / Linux:
# python3 -m venv venv_folder
# source venv_folder/bin/activate
# pip install requests

# Step 2: Python Script (check_requests.py)
import requests

print(f"Requests version: {requests.__version__}")