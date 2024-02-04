import pandas as pd

# Read a CSV file into a Pandas DataFrame
data = pd.read_csv('data.csv')

# Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(data.head())

# Calculate some basic statistics
print("\nBasic Statistics:")
print("Total rows:", len(data))
print("Mean of 'Age' column:", data['Age'].mean())
print("Maximum value in 'Salary' column:", data['Salary'].max())

# Filter the data based on a condition
filtered_data = data[data['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered_data)

# Group data by a column and calculate aggregate statistics
grouped_data = data.groupby('Department')['Salary'].mean().reset_index()
print("\nAverage Salary by Department:")
print(grouped_data)

# Save the filtered data to a new CSV file
filtered_data.to_csv('filtered_data.csv', index=False)
print("\nFiltered data saved to 'filtered_data.csv'")
