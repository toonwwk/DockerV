import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class TitleLabel(QWidget):
    def __init__(self, title):
        QWidget.__init__(self, None)
        layout = QVBoxLayout()
        self.titleLabel = QLabel(title)
        self.titleLabel.setMargin(0)
        self.titleLabel.setStyleSheet('font-size: 20pt; font-weight:bold;')
        layout.addWidget(self.titleLabel)
        layout.setMargin(0)
        self.setLayout(layout)

    def changeTitle(self, newTitle):
        self.titleLabel.setText(newTitle)

