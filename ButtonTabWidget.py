import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
class ButtonWidget(QWidget):
    def __init__(self, number_of_buttons):
        QWidget.__init__(self, None)

        self.button_list = []
        self.layout = QHBoxLayout()

        self.layout.setAlignment(Qt.AlignLeft)
        self.layout.setSpacing(10)
        self.layout.setMargin(0)
        self.setLayout(self.layout)

        self.createButton(number_of_buttons)
    
    def createButton(self, number_of_buttons):
        for  _ in range (number_of_buttons):
            button = QPushButton("Button")
            self.button_list.append(button)
            self.layout.addWidget(button)
    
    def getButtonList(self):
        return self.button_list

    # set buttons title and color
    def setupButtons(self, titleList, colorList):
        for index in range (len(self.button_list)):
            button = self.button_list[index]
            button.setFixedHeight(27)
            title = titleList[index]
            style = 'QPushButton {font-size: 10pt; color: white; background-color: ' + colorList[index] + '; border-color: rgb(255, 255, 255);}'
            clicked_style = 'QPushButton:pressed { background-color: black }'
            button.setText(title)
            button.setStyleSheet(style + clicked_style)



