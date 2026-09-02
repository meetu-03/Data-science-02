#Download a sample CSV file of IPL match scores (you can create your own with columns: match_id, team1, team2, winner) and write a Python script to read the file and print the winner of each match using the csv module.

import csv

with open("ipl_match_scores.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Match", row["match_id"], "Winner:", row["winner"])