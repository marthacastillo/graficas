import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import csv
prueba= pd.read_csv("/home/administradorcito/graficas/final.csv")
#print(prueba.head())
#print(prueba.describe())
#print("Rating",prueba['rating'].describe())
ratings = prueba[['rating','title','user_id']]
#print(ratings.head())
rag= ratings.groupby(['title','rating']).sum()
print(rag.unstack().head(),"\t")


my_plot = rag.unstack().plot(kind='bar',width=0.8,title="Menciones por usuario",stacked=False,figsize=(10,7))
my_plot.set_ylabel("Menciones")
#my_plot.set_title("Menciones por usuario")
my_plot.legend(["0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0"],ncol=10,loc='upper center', bbox_to_anchor=(0.5, -0.99), fancybox=True)
#my_plot.legend(bbox_to_anchor=(1, 1), borderaxespad=-0.1)
plt.tight_layout()

plt.savefig("Histograma.png",dpi=300, format='png',  bbox_inches='tight')
