import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

# class Test(QWidget):
#     def __init__(self):
#         QWidget.__init__(self, None)
#         layout = QVBoxLayout()
#         labelTab = ClickabelLableTab(2, ['button1', 'button2'])
#         layout.addWidget(labelTab)

#         bl = labelTab.getLabelList()
#         bl[0].clicked.connect(self.press1)
#         bl[1].clicked.connect(self.press2)

#         self.setLayout(layout)
    
#     def press1(self):
#         print('button1')

#     def press2(self):
#         print('button2')

class ClickableLabelTab(QWidget):
    def __init__(self, number_of_lable, text_list):
        QWidget.__init__(self, None)
        self.label_list = []
        self.num_lable = number_of_lable
        self.text_list = text_list
        self.setupLabel()

    def setupLabel(self):
        layout = QHBoxLayout(self)
        layout.setSpacing(15)
        layout.setAlignment(Qt.AlignLeft)
        for i in range (self.num_lable):
            button = ClickableLabel(self.text_list[i])
            layout.addWidget(button)
            self.label_list.append(button)
    
    def getLabelList(self):
        return self.label_list
    
class ClickableLabel(QLabel):
    clicked = Signal()
    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)

