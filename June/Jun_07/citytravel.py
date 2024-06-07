import pandas as pd

# Load the data from a CSV file
# The CSV should have columns: 'City', 'Population', 'Airport_Traffic'
data = pd.read_csv('us_cities_airport_traffic.csv')

# Define criteria for 'smaller cities' and 'relatively busy airports'
max_population = 500000  # Example criterion for smaller city
min_airport_traffic = 1000000  # Example criterion for busy airport (in terms of passengers per year)

# Filter the data based on criteria
filtered_data = data[(data['Population'] <= max_population) & (data['Airport_Traffic'] >= min_airport_traffic)]

# Sort the filtered data by airport traffic for better readability
filtered_data = filtered_data.sort_values(by='Airport_Traffic', ascending=False)

# Display the filtered and sorted data
print(filtered_data)

# Save the filtered data to a new CSV file if needed
filtered_data.to_csv('filtered_us_cities_airport_traffic.csv', index=False)
