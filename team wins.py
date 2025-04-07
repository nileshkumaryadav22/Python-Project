import numpy as np
import pandas as pd


data = np.genfromtxt('C:\\Users\\acer\\Downloads\\datasetpython.csv', delimiter=',', dtype=str, skip_header=1)


dates = np.char.strip(data[:, 2], '"')
home_teams = data[:, 3]
away_teams = data[:, 4]
home_goals = np.char.strip(data[:, 5], '"').astype(int)
away_goals = np.char.strip(data[:, 6], '"').astype(int)
results = data[:, 7]


match_summary = []

for i in range(len(dates)):
    match_summary.append({
        "Date": dates[i],
        "HomeTeam": home_teams[i],
        "AwayTeam": away_teams[i],
        "HomeGoal": home_goals[i],
        "AwayGoal": away_goals[i],
        "Result": results[i]
    })


df = pd.DataFrame(match_summary)


print("Match Summary:\n")
print(df.to_string(index=False))
