import numpy as np
import pandas as pd

# Sample dataset with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [3, np.nan, 7, np.nan, 9],
    'C': [np.nan, 2, 3, 4, np.nan]
}
df = pd.DataFrame(data)

def impute_missing_values(df):
    # Calculate mean for each column
    column_means = df.mean()
    
    # Impute missing values with column means
    df_imputed = df.fillna(column_means)
    
    return df_imputed

# Impute missing values
df_imputed = impute_missing_values(df)
print("Imputed DataFrame:")
print(df_imputed)