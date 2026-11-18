import sqlite3

def get_db_connection():
    """Establish a connection to a local SQLite database file"""
    conn = sqlite3.connect("test_qa.db")
    # This allows us to access columns by name (like a dictionary)
    conn.row_factory = sqlite3.Row
    return conn

def setup_test_database():
    """Create a mock users table and insert test data"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Drop table if it exists to start fresh
    cursor.execute("DROP TABLE IF EXISTS users;")
    
    # Create table
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            status TEXT NOT NULL
        );
    """)
    
    # Insert a test record (Data Seeding)
    cursor.execute("INSERT INTO users (username, status) VALUES (?, ?);", ("standard_user", "active"))
    
    conn.commit()
    conn.close()

def query_user_status(username: str):
    """Query the database for a user's status (Backend Validation)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT status FROM users WHERE username = ?;", (username,))
    row = cursor.fetchone()
    
    conn.close()
    return row["status"] if row else None