import sys

from PySide6.QtWidgets import QApplication

from models.itemModel import ItemModel
from models.OrderModel import OrderModel
from controllers.database_manager import DatabaseManager
from views.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    db = DatabaseManager("database.db")
    db.connect()

    itemModel = ItemModel(db)
    orderModel = OrderModel(db)

    mainWindow = MainWindow(itemModel, orderModel)

    mainWindow.show()

    db.disconnect()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
