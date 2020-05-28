import sys
from PySide2.QtWidgets import *
from pyside_material import apply_stylesheet
from PySide2.QtCore import *
from PySide2.QtGui import *


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
        self.cancel.clicked.connect(self.cancelButtonIsClicked)
        self.exec_()

    def cancelButtonIsClicked(self):
        self.close()


class CreateContainerForm(QDialog):
    def __init__(self, parent=None):
        super(CreateContainerForm, self).__init__(parent)

        self.name = QLabel('Name')
        self.image = QLabel('Image')
        self.review = QLabel('Port Mapping')
        self.env = QLabel('Environmental variables')

        self.nameEdit = QLineEdit()
        self.imageEdit = QLineEdit()
        self.reviewEdit = QTextEdit()
        self.envEdit = QTextEdit()

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.name, 1, 0)
        self.grid.addWidget(self.nameEdit, 1, 1)

        self.grid.addWidget(self.image, 2, 0)
        self.grid.addWidget(self.imageEdit, 2, 1)

        self.grid.addWidget(self.review, 3, 0)
        self.grid.addWidget(self.reviewEdit, 3, 1, 1, 1)

        self.grid.addWidget(self.env, 6, 0)
        self.grid.addWidget(self.envEdit, 6, 1, 2, 1)

        self.ok = QPushButton("Ok")
        self.grid.addWidget(self.ok, 10, 0)

        self.cancel = QPushButton("Cancel")
        self.grid.addWidget(self.cancel, 10, 1, 1, 1)
        self.cancel.clicked.connect(self.cancelButtonIsClicked)

        self.setLayout(self.grid)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Create container')

        self.exec_()

    def cancelButtonIsClicked(self):
        self.close()

    def getOk(self):
        return self.ok


if __name__ == "__main__":
    print("foo")
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_red.xml')
    ex = CreateContainerForm()

    # sys.exit(app.exec_())
