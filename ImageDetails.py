import sys

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ClickableLabel import ClickableLabel
from pyside_material import apply_stylesheet


class ImageDetails(QWidget):
    def __init__(self, imageDetail: list):
        QWidget.__init__(self, None)
        self.imageDetail = imageDetail
        self.formatString()
        self.image_id = ClickableLabel(self.imageDetail[0])
        self.image_tag = ClickableLabel(self.imageDetail[1])
        self.image_size = ClickableLabel(self.imageDetail[2])
        self.image_date = ClickableLabel(self.imageDetail[3])

        self.image_id.clicked.connect(self.press1)
        self.check_box = QCheckBox()

        layout = QHBoxLayout(self)
        layout.setSpacing(15)
        layout.addWidget(self.check_box)
        layout.addWidget(self.image_id)
        layout.addWidget(self.image_tag)
        layout.addWidget(self.image_size)
        layout.addWidget(self.image_date)
        layout.setAlignment(Qt.AlignLeft)

        
        self.setLayout(layout)


    def press1(self):
        print("pressed")

    def formatString(self):
        unit_list = ['KB', 'MB', 'GB']
        size = int(self.imageDetail[2])
        count = -1
        while size > 1024:
            count += 1
            size /= 1024
        
        size = format(size, '.1f')
        self.imageDetail[2] = str(size) + unit_list[count]

        date = self.imageDetail[3]
        self.imageDetail[3] = date[0 : 10] + ':' + date [11 : 19]

    def getCheckbox(self):
        return self.check_box
    
    def getTag(self):
        return self.imageDetail[1]



