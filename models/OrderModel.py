from datetime import datetime


class OrderModel:
    def __init__(self, database):
        self.db = database
        query = ("CREATE TABLE IF NOT EXISTS orders ("
                 "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "total REAL NOT NULL,"
                 "profit REAL NOT NULL,"
                 "items VARCHAR(400) NOT NULL,"
                 "date_time TEXT NOT NULL )")
        try:
            self.db.execute_query(query)
            print("Table created")
        except Exception as e:
            print("Table creation error: ", e)

    def addOrderToDb(self, total: float, profit: float, items: str):
        query = ("INSERT INTO orders "
                 "(total, profit, items, date_time) "
                 "VALUES (?, ?, ?, ?)")
        values = (total, profit, items, datetime.now().strftime("%Y-%m-%d"))

        try:
            self.db.execute_query(query, values)
            print("Item added")
        except Exception as e:
            print("Item addition error: ", e)

    def getOrders(self, **kwargs):  # FIXME я це буду рахувати як перегружену функцію, бо вона приймає різну кількість аргументів і в залежності від цього виконується різний код
        fields = 'AND '.join([f"{key} = ?" for key in kwargs.keys()])
        query = f"SELECT * FROM orders WHERE {fields}"
        values = tuple(kwargs.values())

        try:
            return self.db.fetch_query(query, values)
        except Exception as e:
            print("Item fetch error: ", e)
            return []

    # Przeciążanie funkcji nie jest obsługiwane w Pythonie, ponieważ Python używa dynamicznego typowania,
    # a zatem nie może określić, która wersja funkcji ma zostać wywołana przed uruchomieniem.

    def get_next_id(self) -> int:
        query = "SELECT MAX(id) FROM orders"
        try:
            result = self.db.fetch_query(query)
            max_id = result[0][0]
            if max_id is None:
                return 1
            else:
                return max_id + 1
        except Exception as e:
            print("Error fetching max id: ", e)
            return None