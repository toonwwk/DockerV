from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class VolumeItem(QWidget):
    def __init__(self, name, driver, point, created, is_header = False):
        super(VolumeItem, self).__init__()
        
        layout = QHBoxLayout(self)
    
        self.check_box = QCheckBox()
        self.check_box.setMinimumSize(50 ,50)
        
        if is_header:
            self.check_box.hide()
            temp = QLabel()
            temp.setMinimumSize(50 ,50)
            layout.addWidget(temp)

        self.name = QLabel(name)
        self.name.setMinimumSize(100, 50)
        self.point = QLabel(point)
        self.point.setMinimumSize(300, 50)
        self.driver = QLabel(driver)
        self.driver.setMinimumSize(100, 50)
        self.created = QLabel(created)
        self.created.setMinimumSize(100, 50)

        layout.addWidget(self.check_box)
        layout.addWidget(self.name)
        layout.addWidget(self.driver)
        layout.addWidget(self.point)
        layout.addWidget(self.created)

        self.setLayout(layout)
    
    def get_checkbox(self):
        return self.check_box
        


