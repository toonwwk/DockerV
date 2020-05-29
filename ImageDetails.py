import sys

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ClickableLabel import ClickableLabel
from pyside_material import apply_stylesheet


class ImageDetails(QWidget):
    def __init__(self, imageDetail: list, is_header = False):
        QWidget.__init__(self, None)
        self.imageDetail = imageDetail

        self.check_box = QCheckBox()
        self.check_box.setMinimumSize(50, 50)
        layout = QHBoxLayout(self)


        if not is_header:
            self.formatString()
        else:
            self.check_box.hide()
            temp = QLabel()
            temp.setMinimumSize(50, 50)
            layout.addWidget(temp)

        
        self.image_id = ClickableLabel(self.imageDetail[0])
        self.image_id.setMinimumSize(650, 50)
        self.image_tag = ClickableLabel(self.imageDetail[1])
        self.image_tag.setMinimumSize(70, 50)
        self.image_size = ClickableLabel(self.imageDetail[2])
        self.image_size.setMinimumSize(80, 50)
        self.image_date = ClickableLabel(self.imageDetail[3])
        self.image_date.setMinimumSize(200, 50)        

        layout.setSpacing(10)
        layout.addWidget(self.check_box)
        layout.addWidget(self.image_id)
        layout.addWidget(self.image_tag)
        layout.addWidget(self.image_size)
        layout.addWidget(self.image_date)
        layout.setAlignment(Qt.AlignLeft)

        
        self.setLayout(layout)

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

    def getId(self):
        return self.imageDetail[0]



