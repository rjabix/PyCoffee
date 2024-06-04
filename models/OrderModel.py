
class OrderModel:
    def __init__(self, database):
        self.db = database
        query = ("CREATE TABLE IF NOT EXISTS orders ("
                 "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "total INTEGER NOT NULL,"
                 "profit REAL NOT NULL,"
                 "items VARCHAR(400) NOT NULL )")
        try:
            self.db.execute_query(query)
            print("Table created")
        except Exception as e:
            print("Table creation error: ", e)

    def addOrderToDb(self, total: float, profit: float, items: str):
        query = ("INSERT INTO items "
                 "(total, profit, items) "
                 "VALUES (?, ?, ?)")
        values = (total, profit, items)

        try:
            self.db.execute_query(query, values)
            print("Item added")
        except Exception as e:
            print("Item addition error: ", e)

    def getOrders(self, **kwargs):  # type = 0 nprz
        fields = 'AND '.join([f"{key} = ?" for key in kwargs.keys()])
        query = f"SELECT * FROM orders WHERE {fields}"
        values = tuple(kwargs.values())

        try:
            return self.db.fetch_query(query, values)
        except Exception as e:
            print("Item fetch error: ", e)
            return []