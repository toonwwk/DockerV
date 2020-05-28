import sys
import os
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from GIFWidget import ImagePlayer

class Homepage(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.layout = QVBoxLayout(self)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(base_dir, 'images', 'docker_gif3.gif')
        self.image = ImagePlayer(self.image_path)   
        self.image.setFixedSize(500,500)
        
        self.label = QLabel(' DOCKER V')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-family: Optima; font-size: 40pt;')
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.label)
        self.layout.setAlignment(Qt.AlignCenter)
        




