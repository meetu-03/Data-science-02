# Task 3
# Question:
# Use the datetime module to get the current date and time, then format and print it as 'DD-MM-YYYY HH:MM:SS', similar to how WhatsApp shows message timestamps.
# Hint: Use strftime() to format the output.

# Answer:


from datetime import datetime

# Get current date and time
now = datetime.now()

# Format as 'DD-MM-YYYY HH:MM:SS'
formatted_time = now.strftime("%d-%m-%Y %H:%M:%S")
print(f"Timestamp: {formatted_time}")