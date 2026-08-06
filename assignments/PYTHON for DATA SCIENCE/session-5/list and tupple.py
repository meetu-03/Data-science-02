# 1.Create a list called playlist_ids with 5 song IDs (as integers) that you might see in a Spotify playlist, and print the list.

# ANSWER...

playlist_ids = [101, 102, 103, 104, 105]
print(playlist_ids) 



# 2.Add two more song IDs to your playlist_ids list using both append() and extend(), then print the updated list.<br><br><em><strong>Hint:</strong> Use append() for a single ID and extend() for adding multiple IDs at once.</em>

# ANSWER...

playlist_ids.append(106)  # Adding a single song ID
playlist_ids.extend([107, 108])  # Adding multiple song IDs
print(playlist_ids)


# 3.Simulate removing the last played song from your playlist_ids list using pop(), and display the removed ID along with the remaining playlist. 4.

# ANSWER...

removed_song_id = playlist_ids.pop()  # Remove the last song ID
print("Removed song ID:", removed_song_id) 

# 4.Create a tuple called insta_filters with 4 Instagram filter names (as strings). Try to change the first filter name and observe what error you get.<br><br><em><strong>Hint:</strong> Tuples are immutable. Note down the error message.</em>

# ANSWER...


insta_filters = ('Clarendon', 'Gingham', 'Juno', 'Lark')    
insta_filters[0] = 'Velogra'  # This will raise a TypeError
print(insta_filters)


# 5.Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names) and prints which one should use a list and which should use a tuple, explaining your choice in a comment.

# ANSWER...


# Scenario: A list of recent Zomato orders vs a tuple of fixed IPL team names
zomato_orders = ['Pizza', 'Burger', 'Pasta']  # Use a list because the orders can change
ipl_teams = ('Mumbai Indians', 'gujrat titans', 'Royal Challengers Bangalore', 'Kolkata Knight Riders')  # Use a tuple because the team names are fixed
print("Zomato orders (list):", zomato_orders)
print("IPL teams (tuple):", ipl_teams)

