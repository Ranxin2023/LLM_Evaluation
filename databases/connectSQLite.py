import os
import sqlite3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the database path from environment variables
db_path = os.getenv("DATABASE_PATH")
print("Database path is:", db_path)
if not db_path:
    raise ValueError("No database path found. Please set the DATABASE_PATH in the .env file.")

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
if conn:
    print("Connection successfully established")

cursor = conn.cursor()

# Create the 'models' table if it doesn't exist
create_table_cmd = '''
CREATE TABLE IF NOT EXISTS models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT NOT NULL,
    f1_score REAL NOT NULL
)
'''
cursor.execute(create_table_cmd)
print("Table 'models' verified/created successfully")

# Insert initial data into the 'models' table
new_row = ["ChatGPT", 0.80]
cmd = '''INSERT INTO models (model_name, f1_score) VALUES(?, ?)'''
cursor.execute(cmd, new_row)
conn.commit()
print("Data inserted successfully")

# Verify the inserted data
cursor.execute("SELECT * FROM models")
rows = cursor.fetchall()
print("Current rows in 'models' table:")
for row in rows:
    print(row)

# Close the connection
conn.close()
print("Connection closed successfully")
