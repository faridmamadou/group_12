"""
Tâche 2:
3. Scatter en R
"""

# Importons les bibliothèques nécessaires

library(ggplot2)
library(readr)
library(viridis)

# Chargeons le dataset

df <- read_csv("Tache_2\\Housing_cleaned.csv")

# Réalisons le scatter

scatter <- ggplot(df, aes(x=area, y=price, color=factor(bedrooms), size=75)) +
  geom_point(size = 3, alpha =  0.7) +
  scale_color_viridis(discrete = TRUE) +
  labs(
    title = "Evolution du prix en fonction de la surface\n",
    x = "\nArea",
    y = "Price\n",
    color = "Bedrooms"
  ) +
  theme_minimal() +
  theme (
    plot.title = element_text(size = 18, hjust = 0.4, face = "bold"),
    axis.title.x = element_text(size = 14),
    axis.title.y = element_text(size = 14)
  )

print(scatter)