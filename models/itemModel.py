
class ItemModel:

    def __init__(self, database):
        self.db = database
        query = ("CREATE TABLE IF NOT EXISTS items ("
                 "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "type INTEGER NOT NULL,"
                 "name VARCHAR(100) NOT NULL,"
                 "price REAL NOT NULL,"
                 "cost REAL NOT NULL,"
                 "photourl VARCHAR(100))")
        try:
            self.db.execute_query(query)
            print("Table created")
        except Exception as e:
            print("Table creation error: ", e)

    def addItemToDb(self, itemtype, name, price, cost, url):
        query = ("INSERT INTO items "
                 "(type, name, price, cost, photourl) "
                 "VALUES (?, ?, ?, ?, ?)")
        values = (itemtype, name, price, cost, url)

        try:
            self.db.execute_query(query, values)
            print("Item added")
        except Exception as e:
            print("Item addition error: ", e)

    def getItems(self, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            if isinstance(value, str) and value.endswith('*'):
                fields.append(f"{key} LIKE ?")
                values.append(value[:-1] + '%')  # Replace '*' with '%' for SQL wildcard searches
            else:
                fields.append(f"{key} = ?")
                values.append(value)
        fields = ' AND '.join(fields)
        query = f"SELECT * FROM items WHERE {fields}"
        values = tuple(values)

        try:
            return self.db.fetch_query(query, values)
        except Exception as e:
            print("Item fetch error: ", e)
            return []

    def deleteItem(self, name):
        query = "DELETE FROM items WHERE name = ?"

        try:
            self.db.execute_query(query, (name,))
            print("Item deleted")
        except Exception as e:
            print("Item deletion error: ", e)

    def updateItem(self, name, **kwargs):
        fields = ', '.join([f"{key} = :{key}" for key in kwargs.keys()])
        query = f"UPDATE items SET {fields} WHERE name = :name"
        kwargs['name'] = name
        try:
            self.db.execute_query(query, kwargs)
            print("Item updated")
        except Exception as e:
            print("Item update error: ", e)
