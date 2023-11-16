# Display basic information about the dataset
import pandas as pd
import waste_detect as w
import matplotlib.pyplot as plt
import seaborn as sns


# Assuming you have already loaded your dataset into the 'data' DataFrame

# Select the columns of interest
columns_of_interest = ['quantity_in_grams', 'ingredient_count', 'waste_in_grams']
subset_data = w.data[columns_of_interest]

# Create a correlation matrix
correlation_matrix = subset_data.corr()

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
