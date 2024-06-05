from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QHBoxLayout

from views.MenuItemButton import MenuItemButton


class CartItemButton(MenuItemButton):
    number_changed = Signal()

    def __init__(self, name: str, price, image_path):
        self.number = 1
        self._name = name
        self.price = price
        super().__init__(name, price, image_path)
        # super().right_vertical_layout.removeWidget(super().right_vertical_layout.itemAt(1).widget())

        self.right_vertical_layout.itemAt(1).widget().setText(f"{str(price)} zł x {self.number}")

        self.font.setFamily("EB Garamond")
        self.font.setPointSize(20)
        self.right_vertical_layout.itemAt(1).widget().setFont(self.font)

        self.add_button = QPushButton("Dodać")
        self.add_button.setFont(self.font)
        self.add_button.clicked.connect(self.add_item)

        self.remove_button = QPushButton("Usunąć")
        self.remove_button.setFont(self.font)
        self.remove_button.clicked.connect(self.remove_item)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.add_button)
        self.horizontal_layout.addWidget(self.remove_button)
        self.right_vertical_layout.addLayout(self.horizontal_layout)

    def add_item(self):
        self.number += 1
        self.right_vertical_layout.itemAt(1).widget().setText(f"{str(self.price)} zł x {self.number}")
        self.number_changed.emit()

    def remove_item(self):
        self.number -= 1
        self.right_vertical_layout.itemAt(1).widget().setText(f"{str(self.price)} zł x {self.number}")
        if self.number == 0:
            self.deleteLater()
        self.horizontal_layout.addWidget(self.add_button)
        self.horizontal_layout.addWidget(self.remove_button)
        self.right_vertical_layout.addLayout(self.horizontal_layout)
        self.number_changed.emit()
