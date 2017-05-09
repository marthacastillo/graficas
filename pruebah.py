import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt 
import csv


prueba= pd.read_csv("/home/administradorcito/graficas/final.csv")
print(prueba.head())
print(prueba.describe())
print("Rating",prueba['rating'].describe())
ratings = prueba[['rating','user_id']]
ratings.head()
# rating_group = ratings.groupby(['title','user_id']).sum()
# print(rating_group)
# print(rating_group.unstack().head())
# mygra= rating_group.unstack().plot(kind ='bar', stacked=True,title="Menciones por usuario")
# mygra.set_xlabel("user_id")
# mygra.set_ylabel("rating")
# plt.tight_layout()
# plt.savefig("his.png")
user_m = ratings['rating'].hist(bins=20)
user_m.set_title("Histograma")
user_m.set_xlabel("Rating")
user_m.set_ylabel("Menciones")
plt.tight_layout()
plt.savefig("Histograma.png")

