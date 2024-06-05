from PySide6.QtWidgets import QMessageBox

from models.itemModel import ItemModel
from controllers.CartController import CartController


class MenuController:
    def __init__(self, itemModel: ItemModel):
        self.itemModel = itemModel
        self.cartController = CartController(itemModel)

    def get_items_by_type(self, type):
        self.itemModel.db.connect()
        data = self.itemModel.getItems(type=type)
        self.itemModel.db.disconnect()
        return data

    def add_item_to_cart(self, name):
        try:
            self.cartController.add(name)
        except Exception as message:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Już w koszyku")
            msg_box.setText(str(message))
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()

    def get_items_by_name(self, name: str):
        self.itemModel.db.connect()
        data = self.itemModel.getItems(name=f'{name.capitalize()}*')
        self.itemModel.db.disconnect()
        return data
