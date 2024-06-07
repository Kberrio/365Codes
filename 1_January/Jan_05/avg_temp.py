import random

# Generate random daily temperature data for a week (7 days)
temperature_data = [random.randint(50, 100) for _ in range(7)]

# Calculate the average temperature for the week
average_temperature = sum(temperature_data) / len(temperature_data)

# Determine if it was a hot or cold week based on the average temperature
if average_temperature >= 80:
    weather_summary = "It was a hot week!"
elif average_temperature >= 60:
    weather_summary = "The weather was pleasant."
else:
    weather_summary = "It was a cold week."

# Print the daily temperatures and the average temperature
print("Daily Temperatures:")
for day, temperature in enumerate(temperature_data, start=1):
    print(f"Day {day}: {temperature}°F")

print(f"\nAverage Temperature for the Week: {average_temperature:.2f}°F")
print(weather_summary)
