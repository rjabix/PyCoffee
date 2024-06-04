import sys

from PySide6.QtWidgets import QApplication

from models.itemModel import ItemModel
from controllers.database_manager import DatabaseManager
from views.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    db = DatabaseManager("database.db")
    db.connect()
    itemModel = ItemModel(db)
    mainWindow = MainWindow(itemModel)
    mainWindow.show()

    db.disconnect()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
