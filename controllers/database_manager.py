import sqlite3


class DatabaseManager:

    def __init__(self, db_name):
        self.conn = None
        self.db_name = db_name

    # Connect to the database
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            print("Connected")
        except sqlite3.Error as e:
            print(f"Database Error: {e}")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Disconnected")

    # Execute a query. If values are provided, bind them to the query
    def execute_query(self, query, values=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, values or [])
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Query Error: {e}")

    # Fetch data from the database like SELECT queries
    def fetch_query(self, query, values=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, values or [])
            data = cursor.fetchall()
            return data
        except sqlite3.Error as e:
            print(f"Query Error: {e}")
            return []
