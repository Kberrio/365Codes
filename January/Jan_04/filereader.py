import pandas as pd

def analyze_csv_file(filename):
    try:
        # Read the CSV file into a Pandas DataFrame
        data = pd.read_csv(filename)
        
        # Display basic statistics
        print("Summary Statistics:")
        print(data.describe())

        # Display data types of each column
        print("\nData Types:")
        print(data.dtypes)

        # Display the first few rows of the data
        print("\nFirst Few Rows:")
        print(data.head())
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please enter a valid filename.")
    except pd.errors.EmptyDataError:
        print(f"The file '{filename}' is empty.")

if __name__ == "__main__":
    filename = input("Enter the name of the CSV file: ")
    analyze_csv_file(filename)
