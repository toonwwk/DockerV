import sys

from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ClickableLabel import ClickableLabel, ClickableLabelTab
from pyside_material import apply_stylesheet


class ContainerListItem(QWidget):
    def __init__(self):
        super(ContainerListItem, self).__init__()

        self.check_box = QCheckBox()
        self.container_name = ClickableLabel("Container")
        self.image_name = ClickableLabel("image")
        self.ip = QLabel("127.0.0.11")
        self.ports = ClickableLabel("9000:9000")
        self.ownerships = QLabel("Bay pc")
        self.container_name.clicked.connect(self.labelPressed)
        self.set_ui()

    def set_ui(self):
        layout = QHBoxLayout()
        layout.addWidget(self.check_box)
        layout.addWidget(self.container_name)
        layout.addWidget(self.image_name)
        layout.addWidget(self.ip)
        layout.addWidget(self.ports)
        layout.addWidget(self.ownerships)

        self.setLayout(layout)
        self.show()
    
    def labelPressed(self):
        print('bey')


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.list_widget = QListWidget(self)
        self.list_widget.setFixedSize(800,600)
        custom_item = ContainerListItem()
        item = QListWidgetItem()
        item.setSizeHint(QSize(600,50))
        item.background()
        item.setFlags(Qt.NoItemFlags)
        self.list_widget.addItem(item)
        self.list_widget.setItemWidget(item, custom_item)

        # self.widget = ContainerListItem()
        # self.setWindowTitle("DockerV")
        # self.setCentralWidget(self.widget)
        self.setFixedSize(800,600)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    apply_stylesheet(app, theme='dark_blue.xml', light_secondary = False)
    window.show()

    sys.exit(app.exec_())