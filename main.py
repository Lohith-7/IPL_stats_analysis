import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('cricket_data_2025.csv')

# Remove rows where Year is missing
df = df.dropna(subset=['Year'])

# Drop unnecessary columns
cols_to_drop = [
    'Matches_Batted','Not_Outs','Balls_Faced','Catches_Taken','Stumpings',
    'Matches_Bowled','Balls_Bowled','Runs_Conceded','Wickets_Taken',
    'Best_Bowling_Match','Bowling_Average','Economy_Rate',
    'Bowling_Strike_Rate','Four_Wicket_Hauls','Five_Wicket_Hauls'
]

df = df.drop(columns=cols_to_drop)

# Convert columns to numeric
df[['Year','Runs_Scored','Batting_Strike_Rate']] = df[
    ['Year','Runs_Scored','Batting_Strike_Rate']
].apply(pd.to_numeric)

# Ask user for player
name = input("Enter the player name: ")

# Filter player directly (faster than groupby)
player_df = df[df['Player_Name'] == name]

if player_df.empty:
    print("Player not available")
    exit()

# Sort by year
player_df = player_df.sort_values('Year')
player_df['Year'] = player_df['Year'].astype(int)

# Plot
fig, ax1 = plt.subplots()

ax1.bar(player_df['Year'], player_df['Runs_Scored'],
        color='orange', width=0.6)
ax1.set_xticks(df['Year'])
ax1.set_xlabel('Year')
ax1.set_ylabel('Runs Scored')
for label in ax1.get_xticklabels():
    label.set_rotation(45)

ax2 = ax1.twinx()
ax2.plot(player_df['Year'], player_df['Batting_Strike_Rate'],
         color='blue', marker='o', linewidth=2)
ax2.set_ylabel('Strike Rate')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.title(f"{name}'s performance by year")
plt.tight_layout()
plt.show()