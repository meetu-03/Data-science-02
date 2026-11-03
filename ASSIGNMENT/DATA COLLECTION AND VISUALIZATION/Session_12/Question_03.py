import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create sample scores for 4 IPL teams, 8 matches each
np.random.seed(42)
teams = ["CSK", "MI", "RCB", "KKR"]
team_names = []
runs = []

for team in teams:
    for match in range(8):
        team_names.append(team)
        runs.append(np.random.randint(120, 230))

df = pd.DataFrame({"Team": team_names, "Runs": runs})
sns.set_theme(style="darkgrid")
sns.violinplot(data=df, x="Team", y="Runs", color="lightblue")

plt.title("IPL Run Distribution by Team")
plt.xlabel("Team")
plt.ylabel("Runs")
plt.show()

# Output: Violin plot comparing runs for four IPL teams.
