from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from Graph import Graph

class ContainerStat(QWidget):
    def __init__(self, title1, x_list1, y_list1, title2, x_list2, y_list2, title3, x_list3, y_list3):
        QWidget.__init__(self, None)
        cpu = Graph(title1, x_list1, y_list1)
        memory = Graph(title2, x_list2, y_list2)
        network = Graph(title3, x_list3, y_list3)

        sub_layout = QHBoxLayout()
        sub_layout.addWidget(cpu)
        sub_layout.addWidget(memory)

        layout = QVBoxLayout(self)
        layout.addLayout(sub_layout)
        layout.addWidget(network)

        




