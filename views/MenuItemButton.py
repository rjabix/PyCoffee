from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt


class MenuItemButton(QPushButton):
    def __init__(self, name, price, image_path):
        super().__init__()

        self._name = name

        if image_path:
            self.image_path = image_path
        else:
            self.image_path = "coffe_test.png"

        with open("assets/menuitem_style.qss", "r") as f:
            self.setStyleSheet(f.read())

        layout = QHBoxLayout()

        # Create label for image
        image_label = QLabel()
        pixmap = QPixmap(f"assets/menuitems_photos/{self.image_path}")
        image_label.setPixmap(pixmap)
        if pixmap.isNull():
            image_label.setText("Image not found")
        #image_label.setScaledContents(True)  # Scale image to fit the label
        layout.addWidget(image_label)

        # Create label for text
        name_label = QLabel(self._name)
        name_label.setObjectName("menu_item_name")
        name_label.setAlignment(Qt.AlignRight)

        font = QFont()
        font.setFamily("French Script MT")
        font.setPointSize(25)
        name_label.setFont(font)

        price_label = QLabel(f"{str(price)} zł")
        price_label.setObjectName("menu_item_price")
        price_label.setAlignment(Qt.AlignRight)

        font.setFamily("French Script MT")
        font.setPointSize(15)
        price_label.setFont(font)

        right_vertical_layout = QVBoxLayout()
        right_vertical_layout.addWidget(name_label)
        right_vertical_layout.addWidget(price_label)

        layout.addLayout(right_vertical_layout)
        # Set the layout on the button
        self.setLayout(layout)

        # Ensure the button expands with the layout
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setFixedHeight(200)  # Set fixed height for all buttons

    def __str__(self):
        return self._name
