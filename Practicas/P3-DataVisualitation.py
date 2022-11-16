import pandas as pd
import matplotlib.pyplot as plt
#Practica 3: Data Visualitation
#Edgar Armando Ruiz Dorador 1990126

df = pd.read_csv('rf-clean-data.csv')
pr = df['player_ranking'].tolist()
ty = df['tourney_year'].tolist()



#plt.scatter(ty,pr, label='Ranking ATP 1999-2016', linestyle = 'dotted')
plt.plot(ty,pr, label='Ranking ATP 1999-2016', linestyle = 'dotted')
plt.title("Ranking de Roger Federer")
plt.xlabel("Years")
plt.ylabel("Rank")
plt.savefig("graph/p3_graph.png")
plt.show()
plt.close()

