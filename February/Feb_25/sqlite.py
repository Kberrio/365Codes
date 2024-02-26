import sqlite3

# Function to create a connection and a table
def create_table():
    # Connect to SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect('example.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SQL query to create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_data(name, age):
    # Connect to SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Execute SQL query to insert data
    cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to retrieve data from the table
def retrieve_data():
    # Connect to SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Execute SQL query to retrieve data
    cursor.execute('''SELECT * FROM users''')

    # Fetch all rows
    rows = cursor.fetchall()

    # Print fetched data
    for row in rows:
        print(row)

    # Close connection
    conn.close()

# Main function
def main():
    # Create the table
    create_table()

    # Insert some data
    insert_data('Alice', 30)
    insert_data('Bob', 25)

    # Retrieve and display data
    retrieve_data()

if __name__ == "__main__":
    main()
