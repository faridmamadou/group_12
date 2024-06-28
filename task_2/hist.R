"""
Tâche 2:
2. Histogramme en R
"""

# Importons les bibliothèques nécessaires

library(ggplot2)
library(readr)

# Chargeons le dataset

df <- read_csv('Tache_2\\Housing_cleaned.csv')


# Réalisons l'histogramme

hist <- ggplot(df, aes(x=bedrooms)) +
  geom_histogram(binwidth = 0.5, fill='skyblue', color='black', alpha=0.7) +
  geom_vline(aes(xintercept = median(df$bedrooms)), color='red', linetype='dashed', linewidth=1) +
  geom_vline(aes(xintercept = mean(df$bedrooms)), color='blue', linetype='dotted', linewidth=1) +
  labs(
    title = 'Bedrooms\n',
    x = '\nNombre de chambres',
    y = 'Fréquences\n') +
  theme_minimal() +
  theme (
    plot.title = element_text (size = 18, hjust = 0.45, face = "bold"),
    axis.title.x = element_text (size = 14),
    axis.title.y = element_text (size = 14)
  )

print(hist)