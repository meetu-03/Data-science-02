# 1.Create a Python script that uses a for loop to print the names of 5 favorite food delivery apps (e.g., Zomato, Swiggy, etc.), one per line.

# ANSWER...

food_delivery_apps = ["Zomato", "Swiggy", "Uber Eats", "DoorDash", "EatSure"]

for app in food_delivery_apps:
    print(app)

 # 2.Given a list of daily step counts for a week, use a while loop to find and print the first day when you crossed 10,000 steps.<br><br><em><strong>Hint:</strong> Loop through the list and stop as soon as you find a value greater than 10,000.</em>  
 
 # ANSWER...
   

steps = [7500, 8200, 9500, 10500, 11000, 9800, 12000]

i = 0

while i < len(steps):
    if steps[i] > 10000:
        print("First day crossed 10,000 steps:", i + 1)
        break
    i += 1


# 3.Write a Python function that takes a list of IPL team names and prints only those teams whose names are longer than 6 characters, skipping the rest using the continue statement.
 
# ANSWER...


def print_long_teams(teams):
    for team in teams:
        if len(team) <= 6:
            continue
        print(team)


ipl_teams = ["CSK", "MI", "RCB", "Kolkata Knight Riders", "Rajasthan Royals"]

print_long_teams(ipl_teams)



# 4.You have a list of song durations (in seconds) from your Spotify playlist. Use a for loop with enumerate to print each song's position (starting from 1) and its duration in the format: 'Song 1: 210 seconds'.

#ANSWER...


song_durations = [210, 185, 240, 195, 300]

for i, duration in enumerate(song_durations, start=1):
    print(f"Song {i}: {duration} seconds")


# 5.Build a simple shopping cart total calculator: Given a list of item prices from a Flipkart cart, use a loop to sum the prices. If an item price is 0 (out of stock), skip it. Stop adding items if the running total crosses ₹2000 using break, and print the final total.<br><br><em><strong>Constraint:</strong> Use both break and continue in your solution.</em>    


# ANSWER...


prices = [500, 300, 0, 700, 600, 400]

total = 0

for price in prices:
    if price == 0:
        continue

    total += price

    if total > 2000:
        break

print("Final total: ₹", total)

