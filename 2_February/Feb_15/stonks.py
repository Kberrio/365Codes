import requests

# Function to fetch stock data from Alpha Vantage API
def get_stock_data(symbol):
    api_key = 'YOUR_API_KEY_HERE'  # Replace 'YOUR_API_KEY_HERE' with your Alpha Vantage API key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if there's an error message in the response
        if 'Error Message' in data:
            print("Error:", data['Error Message'])
            return None
        else:
            return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

# Main function
def main():
    symbol = input("Enter the stock symbol: ").upper()
    stock_data = get_stock_data(symbol)
    
    if stock_data:
        print("Stock data for symbol", symbol)
        print(stock_data)  # You can further process and display the stock data here

# Call the main function to execute the program
if __name__ == "__main__":
    main()
