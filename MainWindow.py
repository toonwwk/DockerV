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
from VolumeList import VolumeList
from Dashboard import Dashboard

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(1200 ,800)

        #create side menu 
        self.listView = QListWidget()
        self.listView.setMaximumWidth(120)
        self.listView.itemSelectionChanged.connect(self.on_selection_changed)
        self.listView.ScrollMode(False)

        self.stack = QStackedWidget (self)
        
        # add widget of each page here
        # home dashboard stack service container images volume
        self.homepage = Homepage()
        self.dashboard = Dashboard(1 ,2 ,3 ,4 ,5, self.listView)
        self.stack5 = QWidget()
        self.images = ListImages()
        self.volumes = VolumeList()

        # self.log = Log('text.txt')

        self.stack.addWidget (self.homepage)
        self.stack.addWidget (self.dashboard)
        self.stack.addWidget (self.stack5)
        self.stack.addWidget (self.images)
        self.stack.addWidget (self.volumes)


        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.listView)
        self.layout.addWidget(self.stack)
        self.layout.setSpacing(15)

        self.setLayout(self.layout)
        self.setupMenu()

    def setupMenu(self):
        menuList = ['HOME', 'DASHBOARD', 'CONTAINERS', 'IMAGES', 'VOLUMES']
        for i in range (len(menuList)):
            self.listView.insertItem(i, menuList[i])
            # self.listView.item(i).setFont(QFont('Roboto', 16))

    def on_selection_changed(self):
        index = self.listView.currentRow()
        self.stack.setCurrentIndex(index)
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='dark_blue.xml', light_secondary = True)
    # apply_stylesheet(app, theme='dark_teal.xml', light_secondary = True)
    window.show()

    sys.exit(app.exec_())