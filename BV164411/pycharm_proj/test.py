import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = np.eye(5)

path = "./data/ex1data1.txt"
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
data.head()

data.plot(kind='scatter', x='Population', y='Profit', figsize=(12, 8))
plt.show()
