import sys
from PySide2.QtWidgets import *


class Popup(QDialog):

    def __init__(self, E, parent=None):
        super(Popup, self).__init__(parent)
        self.setWindowTitle("Error")
        self.setMinimumSize(500, 100)
        self.cancel = QPushButton("Ok")
        self.label = QLabel(E)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.cancel)
        self.layout.addWidget(self.label)
        self.exec_()

    def cancelButtonIsClicked(self):
        self.dlg.close()
