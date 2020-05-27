import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from pyside_material import apply_stylesheet

from ButtonTabWidget import ButtonWidget
from TitleWidget import TitleLabel
from Homepage import Homepage
from Log import Log
from Graph import Graph
from ContainerStat import ContainerStat
from Images import ListImages

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(800,600)

        #create side menu 
        self.listView = QListWidget()
        self.listView.setMaximumWidth(120)
        self.listView.itemSelectionChanged.connect(self.on_selection_changed)
        self.listView.ScrollMode(False)

        self.stack = QStackedWidget (self)
        
        # add widget of each page here
        # home dashboard stack service container images config
        self.homepage = Homepage()
        self.log = ContainerStat('CPU USAGE', [0,1,2], [0,1,2], 'MEMORY', [0,1,2], [0,1,2], 'NETWORK', [0,1,2], [0,1,2])
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.stack5 = QWidget()
        self.images = ListImages()
        self.stack7 = QWidget()

        # self.log = Log('text.txt')

        self.stack.addWidget (self.homepage)
        self.stack.addWidget (self.log)
        self.stack.addWidget (self.stack3)
        self.stack.addWidget (self.stack4)
        self.stack.addWidget (self.stack5)
        self.stack.addWidget (self.images)
        self.stack.addWidget (self.stack7)


        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.listView)
        self.layout.addWidget(self.stack)
        self.layout.setSpacing(15)

        self.setLayout(self.layout)
        self.setupMenu()

    def setupMenu(self):
        menuList = ['HOME', 'DASHBOARD', 'STACKS', 'SERVICE', 'CONTAINERS', 'IMAGES', 'CONFIGS']
        for i in range (len(menuList)):
            self.listView.insertItem(i, menuList[i])
            # self.listView.item(i).setFont(QFont('Roboto', 16))

    def on_selection_changed(self):
        index = self.listView.currentRow()
        self.stack.setCurrentIndex(index)
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='dark_blue.xml', light_secondary = False)
    # apply_stylesheet(app, theme='dark_teal.xml', light_secondary = True)
    window.show()

    sys.exit(app.exec_())