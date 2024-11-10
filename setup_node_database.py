import sqlite3

def setup_database():
    conn = sqlite3.connect('node_database.db')  # Use a file-based database
    cursor = conn.cursor()

    # Create the Employees table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      department TEXT,
                      location TEXT
                      )''')

    # Insert sample data into the table
    sample_data = [
        (1, 'Alice', 'Engineering', 'NY'),
        (2, 'Bob', 'HR', 'LA'),
        (3, 'Charlie', 'Engineering', 'SF'),
        (4, 'Daisy', 'Marketing', 'NY'),
        (5, 'Eve', 'Engineering', 'LA')
    ]
    cursor.executemany('INSERT INTO Employees VALUES (?, ?, ?, ?)', sample_data)
    conn.commit()
    print("Database setup completed.")
    conn.close()

if __name__ == "__main__":
    setup_database()
