import pandas as pd
import numpy as np

# Load the k values dataset
path = 'C:/Users/王斯哲/PycharmProjects/pythonProject/'
k_values_df = pd.read_csv(path + 'k_values.csv')

# Remove rows where k values are less than or equal to 0
k_values_df = k_values_df[k_values_df['k'] > 0]

# Remove outliers in k values (using 1.5*IQR rule)
Q1 = k_values_df['k'].quantile(0.25)
Q3 = k_values_df['k'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
k_values_df = k_values_df[(k_values_df['k'] > lower_bound) & (k_values_df['k'] < upper_bound)]

# Reverse mapping of k values to a 0-100 scale for "评分" (score)
max_k = k_values_df['k'].max()
min_k = k_values_df['k'].min()
k_values_df['score'] = 100 * (max_k - k_values_df['k']) / (max_k - min_k)

# Save the updated dataframe to a new CSV file
k_values_df.to_csv(path + 'k_values_with_scores.csv', index=False)

print("The k values with scores have been saved to 'k_values_with_scores.csv'.")

# Display the first few rows of the updated dataframe
print(k_values_df.head())