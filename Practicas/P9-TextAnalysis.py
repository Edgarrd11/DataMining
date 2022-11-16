import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#Practica 9: Text Analysis
#Edgar Armando Ruiz Dorador 1990126

df = pd.read_csv('rf-clean-data.csv')
op = df['opponent_name'].tolist()
combined_text = ' '.join(op)
ta = WordCloud(max_words=100,background_color="white").generate(combined_text)

plt.imshow(ta, interpolation="bilinear")
plt.axis('off')
plt.title("Rivales destacados de Roger Federer")
plt.savefig("graph/p9_graph.png")
plt.show()