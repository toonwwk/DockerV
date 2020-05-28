import os
import sys

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ClickableLabel import ClickableLabel

from pyside_material import apply_stylesheet


class DashboardItem(QWidget):
    def __init__(self, amount: int, image_path: str, name: str):
        QWidget.__init__(self, None)
        
        self.picture = QLabel()
        self.picture.setPixmap(QPixmap(image_path))
        
        self.icon = ClickableLabel(self.picture)    
        self.amount = ClickableLabel(str(amount))
        self.name = ClickableLabel(name)

        self.amount.setStyleSheet('font-size: 16pt;')
        self.name.setStyleSheet('font-size: 16pt;')

        self.icon.clicked.connect(self.press1)
        self.amount.clicked.connect(self.press1)
        self.name.clicked.connect(self.press1)

        self.picture.setFixedSize(100,100)
        self.picture.setScaledContents(True)

        layout = QHBoxLayout(self)
        layout.setSpacing(15)
        layout.addWidget(self.picture)                      
        layout.addWidget(self.amount)
        layout.addWidget(self.name)

        layout.setAlignment(Qt.AlignLeft)

        self.setLayout(layout)

    def press1(self):
        print("pressed")
        


