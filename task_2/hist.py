"""
Tâche 2:
1. Histogramme en Python
"""

# Importons les bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Chargeons le dataset
df = pd.read_csv("./Housing_cleaned.csv")

# Réalisons l'hstogramme

plt.figure(figsize=(10, 6))

plt.hist(df['bedrooms'], bins=10, color='lightblue', edgecolor='black', alpha=0.7)

plt.xlabel('Nombre de chambres\n', fontsize=12)
plt.ylabel('Fréquence\n', fontsize=12)
plt.title('Bedrooms\n', fontsize=16)

plt.axvline(np.median(df['bedrooms']), color='red', linestyle='dashed', linewidth=1.5, label='Médiane')
plt.axvline((df['bedrooms'].mean()), color='blue', linestyle='dotted', linewidth=1.5, label='Moyenne')

plt.legend()

plt.show()
