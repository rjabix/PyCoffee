from models.itemModel import ItemModel
from controllers.database_manager import DatabaseManager


def main():
    db = DatabaseManager("database.db")
    db.connect()
    itemModel = ItemModel(db)
    print(itemModel.getItems(type=1))
    db.disconnect()


if __name__ == "__main__":
    main()
