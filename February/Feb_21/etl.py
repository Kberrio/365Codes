import sqlite3
from datetime import datetime, timedelta

# Database connection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Query to extract data
query = "SELECT id, username, last_login FROM users"
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Transformation: Filter users who have not logged in within the last year
one_year_ago = datetime.now() - timedelta(days=365)
active_users = [row for row in rows if datetime.strptime(row[2], '%Y-%m-%d') > one_year_ago]

# Display active users
for user in active_users:
    print(user)

# Close the connection
conn.close()