"""
Tâche 2:
3. Scatter en Python
"""

# Importons les bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt

# Chargeons le dataset
df = pd.read_csv("./Housing_cleaned.csv")

# Réalisons le scatter

x = df['area']
y = df['price']


plt.figure(figsize=(10, 6))

scatter = plt.scatter(x, y, c=df['bedrooms'], s=75, alpha=0.5, cmap='GnBu')

plt.xlabel('\nArea', fontsize=12)
plt.ylabel('Price\n', fontsize=12)
plt.title('Evolution des prix en fonction de la surface\n', fontsize=16)

plt.colorbar(scatter)

plt.show()
