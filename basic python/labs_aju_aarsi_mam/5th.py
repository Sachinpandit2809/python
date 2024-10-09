import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')

# Function to insert values into the table
def insert_data():
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    # Insert values into the table
    cursor.execute('INSERT INTO user_data (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    print("Data inserted successfully.")

# Function to count the number of rows in the table
def count_rows():
    cursor.execute('SELECT COUNT(*) FROM user_data')
    row_count = cursor.fetchone()[0]
    print(f"Number of rows in the table: {row_count}")

# Example usage:
if __name__ == "__main__":
    while True:
        print("\n1. Insert data")
        print("2. Count rows")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, 3): ")

        if choice == '1':
            insert_data()
        elif choice == '2':
            count_rows()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Close the connection when done
conn.close()
