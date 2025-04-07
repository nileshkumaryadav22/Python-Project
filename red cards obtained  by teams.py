import numpy as np
import pandas as pd


data = np.genfromtxt(r'C:\Users\acer\Downloads\datasetpython.csv', delimiter=',', dtype=str, skip_header=1)

dates = np.char.strip(data[:, 2], '"')
home_teams = data[:, 3]
away_teams = data[:, 4]
home_red_cards = np.char.strip(data[:, 22], '"').astype(int)
away_red_cards = np.char.strip(data[:, 23], '"').astype(int)


matches_with_red_cards = []

for i in range(len(home_teams)):
    if home_red_cards[i] > 0 or away_red_cards[i] > 0:
        matches_with_red_cards.append({
            "Date": dates[i],
            "HomeTeam": home_teams[i],
            "AwayTeam": away_teams[i],
            "HomeRedCard": home_red_cards[i],
            "AwayRedCard": away_red_cards[i]
        })


df = pd.DataFrame(matches_with_red_cards)


print("Matches with at least one red card:\n")
print(df.to_string(index=False))
