#Given two lists — one with cricket team names and one with their IPL points — use zip() to pair each team with its points and print them in the format: 'Team: Mumbai Indians, Points: 18'.


teams = ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bengaluru", "Kolkata Knight Riders"]
points = [18, 16, 14, 12]

for team, point in zip(teams, points):
    print(f"Team: {team}, Points: {point}")