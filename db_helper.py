import sqlite3

def get_db_connection():
    conn = sqlite3.connect("test_qa.db")
    conn.row_factory = sqlite3.Row
    return conn

def setup_test_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users and orders tables
    cursor.execute("DROP TABLE IF EXISTS orders;")
    cursor.execute("""
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            item_name TEXT NOT NULL,
            total_price REAL NOT NULL,
            status TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

def insert_order_record(username: str, item_name: str, total_price: float):
    """Simulate backend order logging during checkout"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (username, item_name, total_price, status) VALUES (?, ?, ?, ?);",
        (username, item_name, total_price, "completed")
    )
    conn.commit()
    conn.close()

def get_latest_order_for_user(username: str):
    """Query backend database for validation"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE username = ? ORDER BY id DESC LIMIT 1;", (username,))
    row = cursor.fetchone()
    conn.close()
    return row