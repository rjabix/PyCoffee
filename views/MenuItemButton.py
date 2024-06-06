from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt


class MenuItemButton(QPushButton):
    def __init__(self, name: str, price, image_path):
        super().__init__()

        self._name = name
        self._text = ''

        split_name = name.split()
        for word in split_name:
            if 1 <= len(word) <= 4:
                self._text += word + ' '
            else:
                self._text += word + '\n'
        del split_name

        if image_path:
            self.image_path = image_path
        else:
            self.image_path = "coffe_test.png"

        with open("assets/menuitem_style.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.layout = QHBoxLayout()

        # Create label for image
        image_label = QLabel()
        pixmap = QPixmap(f"assets/menuitems_photos/{self.image_path}")
        pixmap = pixmap.scaled(175, 175, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        if pixmap.isNull():
            image_label.setText("Image not found")

        image_label.setFixedSize(175, 175)
        #image_label.setScaledContents(True)  # Scale image to fit the label
        image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(image_label)

        # Create label for text
        name_label = QLabel(self._text)
        name_label.setObjectName("menu_item_name")
        name_label.setAlignment(Qt.AlignRight)

        # font
        self.font = QFont()
        self.font.setFamily("EB Garamond")
        self.font.setPointSize(25)
        name_label.setFont(self.font)

        price_label = QLabel(f"{str(price)} zł")
        price_label.setObjectName("menu_item_price")
        price_label.setAlignment(Qt.AlignRight)

        self.font.setFamily("French Script MT")
        self.font.setPointSize(15)
        price_label.setFont(self.font)

        self.right_vertical_layout = QVBoxLayout()
        self.right_vertical_layout.addWidget(name_label)
        self.right_vertical_layout.addWidget(price_label)

        self.layout.addLayout(self.right_vertical_layout)
        # Set the layout on the button
        self.setLayout(self.layout)

        # Ensure the button expands with the layout
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setFixedHeight(200)  # Set fixed height for all buttons

    def __str__(self):
        return self._name

    def __len__(self):
        return len(self._name)
