import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'C:\Users\acer\Downloads\datasetpython.csv')


heatmap_data = df.pivot_table(index='HomeTeam', columns='AwayTeam', values='FTHG', aggfunc='sum', fill_value=0)


plt.figure(figsize=(14, 10))
sns.set_theme(style="white")
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', linewidths=0.5)

plt.title("Heatmap of Goals Scored by Home Teams Against Away Teams", fontsize=16)
plt.xlabel("Away Team")
plt.ylabel("Home Team")
plt.tight_layout()
plt.show()
