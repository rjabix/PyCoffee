from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class MenuItemButton(QPushButton):
    def __init__(self, text, price, image_path):
        super().__init__()

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create label for image
        image_label = QLabel()
        pixmap = QPixmap("assets/menuitems_photos/coffe_test.png")
        image_label.setPixmap(pixmap)
        if pixmap.isNull():
            image_label.setText("Image not found")
        #image_label.setScaledContents(True)  # Scale image to fit the label

        # Create label for text
        text_label = QLabel(f"{text}\n{price}")
        text_label.setAlignment(Qt.AlignRight)

        # Add labels to layout
        layout.addWidget(image_label)
        layout.addWidget(text_label)

        # Set the layout on the button
        self.setLayout(layout)

        # Ensure the button expands with the layout
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setFixedHeight(200)  # Set fixed height for all buttons