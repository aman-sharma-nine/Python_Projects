import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

load_df = load_iris()
load_df.keys

data = load_df['data']

df = pd.DataFrame(data)
df.head()

plt.scatter(df[0],df[1])
plt.scatter(df[2],df[3])
plt.xlabel('sepal length & Width', fontsize=13)
plt.ylabel('Petal length & width', fontsize=13)
plt.show()

#pca
#use feature scaling to turn 4 features into 2 features 
area = df[0]*df[1]
area_petal = df[2]* df[3]
