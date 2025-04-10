import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\acer\Downloads\datasetpython.csv')

home_goals = df.groupby('HomeTeam')['FTHG'].sum()
away_goals = df.groupby('AwayTeam')['FTAG'].sum()


total_goals = home_goals.add(away_goals, fill_value=0).sort_values(ascending=False)


plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")
sns.barplot(x=total_goals.values, y=total_goals.index, palette="viridis")

plt.title('Total Goals Scored by Premier League Teams', fontsize=16)
plt.xlabel('Total Goals')
plt.ylabel('Team')
plt.tight_layout()
plt.show()
