import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cricket_data_2025.csv')

df = df.dropna(subset=['Year'])

df = df.drop(columns=['Matches_Batted','Not_Outs','Balls_Faced','Catches_Taken','Stumpings',
'Matches_Bowled','Balls_Bowled','Runs_Conceded','Wickets_Taken','Best_Bowling_Match',
'Bowling_Average','Economy_Rate','Bowling_Strike_Rate','Four_Wicket_Hauls','Five_Wicket_Hauls'])

df['Year'] = pd.to_numeric(df['Year'])
df['Runs_Scored'] = pd.to_numeric(df['Runs_Scored'])
df['Batting_Strike_Rate'] = pd.to_numeric()

# group by player
cricketers = df.groupby('Player_Name')
name = input("Enter the player name: ")

# get specific player group
try:
    single_player_score = cricketers.get_group(name)
except KeyError:
    print("Player not available")
    exit()
single_player_score = single_player_score.sort_values(by='Year')
single_player_score['Year'] = single_player_score['Year'].astype(int)

# plot
fig, ax1 = plt.subplots()
ax1.bar(single_player_score['Year'],
        single_player_score['Runs_Scored'],
        color='orange',
        width=0.6,
        label='Runs')
ax1.set_xlabel('Year')
ax1.set_ylabel('Runs Scored')

ax2 = ax1.twinx()
ax2.plot(single_player_score['Year'],
         single_player_score['Batting_Strike_Rate'],
         color='blue',
         marker='o',
         linewidth=2,
         label='Strike Rate')
ax2.set_ylabel('Strike Rate')
plt.title(f"{name}'s performance by year")
plt.show()

#print(cricketers['Year'].mean())