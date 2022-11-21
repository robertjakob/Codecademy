#LEARN DATA VISUALIZATION WITH PYTHON
#Visualizing World Cup Data With Seaborn

import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
print(df.head())
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
sns.set_style("whitegrid")
sns.set_context("poster", font_scale = 0.8)
f, ax = plt.subplots(figsize = (18, 7))
ax = sns.barplot(x = df["Year"], y = df["Total Goals"])
ax.set_title("Average Number Of Goals Scored In World Cup Matches By Year")

df_goals = pd.read_csv('goals.csv')
print(df_goals.head())
sns.set_context("notebook", font_scale = 1.25)
f, ax2 = plt.subplots(figsize = (14, 7))
ax2 = sns.boxplot(x = "year", y = "goals", data = df_goals, palette = "Spectral")
ax2.set_title("Goals Distribution")

plt.show()
