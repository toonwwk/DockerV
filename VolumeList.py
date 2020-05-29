import os
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ClickableLabel import ClickableLabel, ClickableLabelTab
from VolumeItem import VolumeItem
from docker_temp import User
from ButtonTabWidget import ButtonWidget

class VolumeList(QWidget):
    def __init__(self, user):
        super(VolumeList, self).__init__()
        self.user = user
        self.checkbox_volume_dic = {}
        self.volume_list = self.user.getVolumeList()
        self.selected_volume_list = []

        self.label = QLabel('VOLUME LIST')
        self.label.setStyleSheet('font-family: Optima; font-size: 40pt; ')
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'images')
        volumes_path = os.path.join(path, 'volumes.png')

        self.volume_pic = QLabel()
        self.volume_pic.setPixmap(QPixmap(volumes_path))



        self.buttonTab = ButtonWidget(3)
        self.buttonTab.setupButtons(['Refresh', 'Add volume', 'Remove'], ['#397D00', 'Red', '#b06a00'])
        self.buttonList = self.buttonTab.getButtonList()
        self.buttonList[0].clicked.connect(self.refresh)
        self.buttonList[1].clicked.connect(self.addButtonIsClicked)
        self.buttonList[2].clicked.connect(self.removeButtonIsClicked)

        self.volume_list_view = QListWidget()
        self.volume_list_view.ScrollMode(True)

        self.setup()


        self.row1 = QHBoxLayout()
        self.row1.setSpacing(40)
        self.row1.addWidget(self.label)
        self.row1.addWidget(self.volume_pic)
        self.row1.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout(self)
        layout.addLayout(self.row1)
        layout.addWidget(self.buttonTab)
        layout.addWidget(self.volume_list_view)
        layout.setSpacing(20)

    
    def setup(self):
        self.createHeader()
        for volume in self.volume_list:
            self.createListItem(volume)
    
    def createHeader(self):
        name = 'Name'
        created = 'Created'
        point = 'Mount Point'
        driver = 'Driver'

        item = QtWidgets.QListWidgetItem(self.volume_list_view)
        item.setSizeHint(QSize(100, 60))
        item.setFlags(Qt.NoItemFlags)

        self.volume_list_view.addItem(item)
        custom_item = VolumeItem(name, driver, point, created, True)
        self.volume_list_view.setItemWidget(item, custom_item)

    def createListItem(self, volume):
        name = volume.name
        created = volume.attrs['CreatedAt']
        point = volume.attrs['Mountpoint']
        driver = volume.attrs['Driver']


        item = QtWidgets.QListWidgetItem(self.volume_list_view)
        item.setSizeHint(QSize(100, 60))
        item.setFlags(Qt.NoItemFlags)

        self.volume_list_view.addItem(item)
        custom_item = VolumeItem(name, driver, point, created)
        self.volume_list_view.setItemWidget(item, custom_item)

        cb = custom_item.get_checkbox()
        self.checkbox_volume_dic[cb] = volume
        cb.stateChanged.connect(lambda state, c = cb:(self.checkboxIsPressed(c)))

    def checkboxIsPressed(self, cb):
        if cb.isChecked():
            self.selected_volume_list.append(self.checkbox_volume_dic[cb])
        else:
            self.selected_volume_list.remove(self.checkbox_volume_dic[cb])
        
        print(self.selected_volume_list)

                
    def addButtonIsClicked(self):
        self.dlg = QDialog(self)
        self.dlg.setWindowTitle("Add Volume")
        label = QLabel("Enter volume name ")
        label.setStyleSheet('font-size: 14pt; font-weight: bold;')
        self.name = QLineEdit()
        self.name.setPlaceholderText('eg. korkrane')
        add_button = QPushButton('Add')
        add_button.clicked.connect(self.addExecuteButtonIsClicked)
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.cancelButtonIsClicked)
        sub_layout1 = QHBoxLayout()
        sub_layout1.addWidget(label)
        sub_layout1.addWidget(self.name)
        sub_layout2 = QHBoxLayout()
        sub_layout2.addWidget(add_button)
        sub_layout2.addWidget(cancel_button)
        sub_layout2.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(self.dlg)
        layout.addLayout(sub_layout1)
        layout.addLayout(sub_layout2)
        layout.setAlignment(Qt.AlignCenter)
        self.dlg.setMinimumSize(500 ,100)
        self.dlg.exec_()

    def addExecuteButtonIsClicked(self):
        volume = str(self.name.text())
        if len(volume) > 0:
            new_volume = self.user.addVolume(volume)
            if new_volume:
                self.createListItem(new_volume)
                self.dlg.close()
            else:
                self.name.setText('')
                self.name.setPlaceholderText('error from server')
        
    def removeButtonIsClicked(self):
        for volume in self.selected_volume_list:
            self.user.removeVolume(volume)
        self.selected_volume_list.clear()
        self.refresh()

    def refresh(self):
        self.volume_list_view.clear()
        self.user.setup()
        self.volume_list = self.user.getVolumeList() 
        self.setup() 

    def cancelButtonIsClicked(self):
        self.dlg.close()
   


        


