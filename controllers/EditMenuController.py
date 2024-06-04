from PySide6.QtWidgets import QMessageBox, QDialog, QPushButton

from models.itemModel import ItemModel


class EditMenuController:
    def __init__(self, itemModel: ItemModel):
        self.itemModel = itemModel

    def add_item_menu(self, type, name, price, cost, url):
        if len(name) > 100 or len(url) > 100:
            raise ValueError("The product name or URL is too long.")

        if not name or not price or not cost:
            raise ValueError("Please fill in all the required fields.")

        self.itemModel.db.connect()
        if self.itemModel.getItems(name=name):
            self.itemModel.db.disconnect()
            raise ValueError("The product name already exists.")

        self.itemModel.addItemToDb(type, name, price, cost, url)
        self.itemModel.db.disconnect()

    def delete_item_menu(self, name):
        if not name:
            raise ValueError("Please fill in the product name.")

        self.itemModel.db.connect()
        if not self.itemModel.getItems(name=name):
            self.itemModel.db.disconnect()
            raise ValueError("The product name does not exist.")

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Delete")
        msg_box.setText("Czy na pewno chcesz usunąć ten wpis?")

        yes_button = QPushButton("Tak")
        no_button = QPushButton("Nie")
        msg_box.addButton(yes_button, QMessageBox.YesRole)
        msg_box.addButton(no_button, QMessageBox.NoRole)

        # Виконуємо діалогове вікно і повертаємо відповідь користувача
        result = msg_box.exec()
        if result != 2:  # двійка, бо якщо нажмаєш так, то повертається 2, хз чому
            return

        self.itemModel.deleteItem(name)
        self.itemModel.db.disconnect()

    def edit_item_menu(self, type, name, price, cost, url):
        if len(name) > 100 or len(url) > 100:
            raise ValueError("The product name or URL is too long.")

        if not name or not price or not cost:
            raise ValueError("Please fill in all the required fields.")

        self.itemModel.db.connect()
        if not self.itemModel.getItems(name=name):
            self.itemModel.db.disconnect()
            raise ValueError("The product name does not exist.")

            # Your logic for adding the product goes here

        self.itemModel.updateItem(name, type=type, price=price, cost=cost, photourl=url)
        self.itemModel.db.disconnect()
