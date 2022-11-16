import pandas as pd
#Practica 2: Data Statistics
#Edgar Armando Ruiz Dorador 1990126

df = pd.read_csv('rf-clean-data.csv')
pr = df['player_ranking']
ts = df['tourney_surface'].tolist()
mwl = df['match_win_loss'].tolist() 

grass = ts.count("Grass")
clay = ts.count("Clay")
hard = ts.count("Hard")
sf = []
sf.append(grass)
sf.append(clay)
sf.append(hard)
mw = max(sf)

if(mw == grass):
    best_sf = "Pasto"
elif(mw == clay): 
    best_sf = "Arcilla"
elif(mw == hard):
    best_sf = "Cancha dura"



    
print("Estadisticas de Roger Federer 1999-2016: ")
print("Puesto de ranking ATP promedio:" + "\n" + str(int(pr.mean().round())))
print("Con una desviacion de: " + "\n" + str(int(pr.std().round())))
print("Total de vitorias: " + "\n" + str(mwl.count('W')))
print("Total de derrotas: " + "\n" + str(mwl.count('L')))
print("Partidos en pasto: " + str(grass))
print("Partidos en arcilla: " + str(clay))
print("Partidos en cancha dura: " + str(hard))
print("Superficie mas frecuente: " + "\n" + best_sf + " con " + str(mw) + " victorias ")

