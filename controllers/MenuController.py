from models.itemModel import ItemModel


class MenuController:
    def __init__(self, database: ItemModel):
        self.db = database

    def get_items_by_type(self, type):
        self.db.db.connect()
        data = self.db.getItems(type=type)
        self.db.db.disconnect()
        return data