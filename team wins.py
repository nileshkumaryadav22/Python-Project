import numpy as np
import pandas as pd

# Load the CSV file
data = np.genfromtxt('C:\\Users\\acer\\Downloads\\datasetpython.csv', delimiter=',', dtype=str, skip_header=1)

# Column indices based on the provided dataset:
# Date = 2, HomeTeam = 3, AwayTeam = 4, FTHG = 5, FTAG = 6, FTR = 7
dates = np.char.strip(data[:, 2], '"')
home_teams = data[:, 3]
away_teams = data[:, 4]
home_goals = np.char.strip(data[:, 5], '"').astype(int)
away_goals = np.char.strip(data[:, 6], '"').astype(int)
results = data[:, 7]

# Create a list of dictionaries
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

# Convert to DataFrame
df = pd.DataFrame(match_summary)

# Print in tabular format
print("Match Summary:\n")
print(df.to_string(index=False))
