import sys
import os
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
class Homepage(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.layout = QVBoxLayout(self)
        self.image = QLabel()
        self.image.setFixedSize(300,300)
        self.label = QLabel(' DOCKER V')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-family: Optima; font-size: 40pt;')
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(base_dir, 'images', 'docker_pic2')
        self.image.setScaledContents(True)
        self.image.setPixmap(QPixmap(self.image_path))
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.label)
        self.layout.setAlignment(Qt.AlignCenter)


