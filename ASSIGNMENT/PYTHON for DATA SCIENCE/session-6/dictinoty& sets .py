# 1.Create a Python dictionary called insta_followers that stores the number of followers for 5 Instagram influencers (use their usernames as keys and follower counts as values). Print the dictionary.

# ANSWER...

insta_followers = {
    'kohali': 1500000,
    'dhoni': 2000000,
    'gill': 1200000,
    'rohit': 1800000,
    'jadeja': 2500000
}

print(insta_followers)


# 2.Create a Python dictionary called insta_followers that stores the number of followers for 5 Instagram influencers (use their usernames as keys and follower counts as values). Print the dictionary.

# ANSWER...


insta_followers = {
    "cristiano": 650000000,
    "instagram": 700000000,
    "leomessi": 500000000,
    "selenagomez": 420000000,
    "therock": 395000000
}

print(insta_followers)


# 3.Given a dictionary called food_prices with 5 Zomato food items as keys and their prices as values, write code to display all items that cost more than ₹200.

# ANSWER...

food_price={"dabeli":35,"panipuri":30,"ghughra":50,"vadapau":25,"paubhaji":255}


for item, price in food_price.items():
    if price > 200:
        print(item, price)


# 4.Create two sets: flipkart_users and myntra_users, each containing 5 unique usernames. Find and print the set of users who have accounts on both platforms using set intersection.
 
# ANSWER...
        

f_user={"meetu","radhu","hetvi","het","prince"}
m_user={"prince","deep","meetu","kevin","om"}

print(f_user.intersection(m_user))


# 5.Write a function get_unique_artists(spotify_playlist1, spotify_playlist2) that takes two sets of artist names and returns a set of all unique artists across both playlists (set union).<br><br><em><strong>Hint:</strong> Use the union() method or the | operator for sets.</em>

# ANSWER...

def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)


spotify_playlist1 = {"Arijit Singh", "Shreya Ghoshal", "Atif Aslam"}
spotify_playlist2 = {"Arijit Singh", "Sonu Nigam", "Neha Kakkar"}

print(get_unique_artists(spotify_playlist1, spotify_playlist2))

