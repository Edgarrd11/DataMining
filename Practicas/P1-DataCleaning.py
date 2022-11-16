import pandas as pd
#Practica 1: Data Cleaning
#Edgar Armando Ruiz Dorador 1990126

#Raw data
df = pd.read_csv('roger-federer-data.csv')
print("First Dataframe: ")
print(df.head())

#Clean data
col = ['player_ranking','tourney_year', 'tourney_name','tourney_location'
,'tourney_dates', 'tourney_conditions', 'tourney_surface'
, 'opponent_name', 'match_win_loss','match_score']
df1 = pd.read_csv('roger-federer-data.csv',usecols = col)
print("Clean dataframe: ")
df1.to_csv('rf-clean-data.csv')
print(df1.head())


