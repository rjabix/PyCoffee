from models.itemModel import ItemModel


class EditMenuController:
    def __init__(self, itemModel: ItemModel):
        self.itemModel = itemModel

    def add_item_menu(self, type, name, price, cost, url):
        if len(name) > 100 or len(url) > 100:
            raise ValueError("The product name or URL is too long.")

        if not name or not price or not cost:
            raise ValueError("Please fill in all the required fields.")

            # Your logic for adding the product goes here
        self.itemModel.db.connect()
        self.itemModel.addItemToDb(type, name, price, cost, url)
        self.itemModel.db.disconnect()

    def delete_item_menu(self, name):
        if not name:
            raise ValueError("Please fill in the product name.")

        self.itemModel.db.connect()
        self.itemModel.deleteItem(name)
        self.itemModel.db.disconnect()
