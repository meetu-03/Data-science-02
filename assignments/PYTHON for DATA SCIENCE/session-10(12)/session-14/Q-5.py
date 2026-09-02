#Task 5: Set up a new virtual environment using venv, activate it, and install the 'requests' package using pip. Write a short script that imports requests and prints the version installed. Hint: Use 'python -m venv venv_folder', then 'pip install requests'.

# Terminal commands to run:
# 1. Create virtual environment: python -m venv venv_folder
# 2. Activate virtual environment (Windows): venv_folder\Scripts\activate
# 3. Activate virtual environment (macOS/Linux): source venv_folder/bin/activate
# 4. Install requests package: pip install requests

# Python script to verify requests installation
import requests

print(f"Requests version: {requests.__version__}")


import requests

print("Installed Requests version:", requests.__version__)