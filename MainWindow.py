import sys
import os
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
from docker_temp import User
from Container import Container


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.user = User()
        self.setMinimumSize(1200 ,800)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'images')

        self.home_path = os.path.join(path, 'docker_image_16.png')
        self.containers_path = os.path.join(path, 'containers_icon.png')
        self.images_path = os.path.join(path, 'images_icon.png')
        self.volumes_path = os.path.join(path, 'volumes_icon.png')
        self.dashboard_path = os.path.join(path, 'dashboard_icon.png')
        
        

        #create side menu 
        self.listView = QListWidget()
        self.listView.setMaximumWidth(140)
        self.listView.itemSelectionChanged.connect(self.on_selection_changed)
        self.listView.ScrollMode(False)

        self.stack = QStackedWidget (self)
        
        # add widget of each page here
        # home dashboard stack service container images volume
        self.homepage = Homepage()
        self.dashboard = Dashboard(1 , self.user.getNumberOfImageList(), self.user.getNumberOfVolumeList(), self.listView)
        
        self.container = Container(self.user)
        self.images = ListImages(self.user)
        self.volumes = VolumeList(self.user)

        # self.log = Log('text.txt')

        self.stack.addWidget (self.homepage)
        self.stack.addWidget (self.dashboard)
        self.stack.addWidget (self.container)
        self.stack.addWidget (self.images)
        self.stack.addWidget (self.volumes)

        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.listView)
        self.layout.addWidget(self.stack)

        self.setLayout(self.layout)
        self.setupMenu()


    def setupMenu(self):
        imageList = [self.home_path,self.dashboard_path,self.containers_path,self.images_path,self.volumes_path]
        menuList = ['HOME', 'DASHBOARD', 'CONTAINERS', 'IMAGES', 'VOLUMES']
        for i in range (len(menuList)):
            itm = QListWidgetItem(menuList[i])
            itm.setIcon(QIcon(imageList[i]))
            self.listView.addItem(itm)



    def on_selection_changed(self):
        index = self.listView.currentRow()
        if index == 1:
            self.dashboard.setup(1 , self.user.getNumberOfImageList(), self.user.getNumberOfVolumeList())

        self.stack.setCurrentIndex(index)
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # app.setStyle('WindowsVista')
    apply_stylesheet(app, theme='dark_blue.xml', light_secondary = False)
    window.show()

    sys.exit(app.exec_())
