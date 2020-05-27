import sys

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtWidgets, QtCore
from ButtonTabWidget import ButtonWidget
from ImageDetails import ImageDetails
from docker_temp import User
from pyside_material import apply_stylesheet
from functools import partial


class ListImages(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.user = User()
        self.images_list = self.user.getImagesList()

        self.checkbox_tag_dic = {}
        self.selected_image_list = []

        self.layout = QVBoxLayout(self)
        
        self.label = QLabel('IMAGES VIEWER')
        self.label.setStyleSheet('font-size: 16pt;')

        self.label2 = QLabel('SEARCH')
        self.label2.setStyleSheet('font-size: 16pt;')
        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.searching)

        self.filterView = None

        self.listImageView = QListWidget()
        self.listImageView.ScrollMode(True)
        self.createImageList(self.images_list)
        
        # Button Setup
        self.buttonTab = ButtonWidget(3)
        self.buttonTab.setupButtons(['Refresh', 'Pull', 'Remove'], ['#397D00', 'Red', '#b06a00'])
        self.buttonList = self.buttonTab.getButtonList()
        self.buttonList[0].clicked.connect(self.refreshButtonIsClicked)
        self.buttonList[1].clicked.connect(self.pullButtonIsClicked)
        self.buttonList[2].clicked.connect(self.removeButtonIsClicked)

        # Row Setup
        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.label)
        self.row1.setAlignment(Qt.AlignLeft)

        self.row2 = QHBoxLayout()
        self.row2.setSpacing(55)
        self.row2.addWidget(self.label2)
        self.row2.addWidget(self.lineEdit)

        # Set Layout
        self.layout.addLayout(self.row1)
        self.layout.addWidget(self.buttonTab)
        self.layout.addLayout(self.row2)
        self.layout.addWidget(self.listImageView)
        
        self.layout.setAlignment(Qt.AlignTop)


    def searching(self):
        keyword = self.lineEdit.text()
        if len(keyword) == 0:
            self.refreshButtonIsClicked()
            return
        temp = []
        for image in self.images_list:
            print(keyword, image.tags[0])
            if keyword in image.tags[0]:
                temp.append(image)
        
        self.images_list = temp
        self.refreshButtonIsClicked(self.images_list)
        return

    def refreshButtonIsClicked(self, images_list = None):
        self.listImageView.clear()
        if images_list == None:
            images_list = self.user.getImagesList()
        self.createImageList(images_list)
        return
    
    def createListItem(self, image_detail):
        item = QtWidgets.QListWidgetItem(self.listImageView)
        item.setSizeHint(QtCore.QSize(100, 60))
        item.setFlags(Qt.NoItemFlags)
        cb = image_detail.getCheckbox()
        self.checkbox_tag_dic[cb] = image_detail.getTag()
        self.listImageView.addItem(item)
        self.listImageView.setItemWidget(item, image_detail)
        cb.stateChanged.connect(lambda state, c = cb:(self.checkboxIsPressed(c)))


    def createImageList(self, image_list):
        self.images_list = image_list
        for i in range(len(image_list)):
            imageDetail = ImageDetails(self.user.getImageDetail(i))
            self.createListItem(imageDetail)
    
    def checkboxIsPressed(self, cb):
        if cb.isChecked():
            self.selected_image_list.append(self.checkbox_tag_dic[cb])
        else:
            self.selected_image_list.remove(self.checkbox_tag_dic[cb])


    def pullButtonIsClicked(self):        
        self.dlg = QDialog(self)
        self.dlg.setWindowTitle("Pull Image")
        label = QLabel("Enter image repository")
        label.setStyleSheet('font-size: 14pt; font-weight: bold;')
        self.reposity = QLineEdit()
        self.reposity.setPlaceholderText('eg. busybox')
        pull_button = QPushButton('Pull')
        pull_button.clicked.connect(self.pullExecuteButtonIsClicked)
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.cancelButtonIsClicked)
        sub_layout1 = QHBoxLayout()
        sub_layout1.addWidget(label)
        sub_layout1.addWidget(self.reposity)
        sub_layout2 = QHBoxLayout()
        sub_layout2.addWidget(pull_button)
        sub_layout2.addWidget(cancel_button)
        sub_layout2.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(self.dlg)
        layout.addLayout(sub_layout1)
        layout.addLayout(sub_layout2)
        layout.setAlignment(Qt.AlignCenter)
        self.dlg.setMinimumSize(500 ,100)
        self.dlg.exec_()
    
    def pullExecuteButtonIsClicked(self):
        image_repo = str(self.reposity.text()) + ':latest'
        image = self.user.pullImage(image_repo)
        if image:
            self.reposity.setPlaceholderText('pull success')
            self.reposity.setText('')
            self.user.addImage(image)
            image_detail = ImageDetails(self.user.getImageDetail(self.user.getNumberOfImageList() - 1))
            self.createListItem(image_detail)
            self.dlg.close()
        else:
            self.reposity.setPlaceholderText('invalid image repository name')
            self.reposity.setText('')
        
    def cancelButtonIsClicked(self):
        self.dlg.close()
    
    def removeButtonIsClicked(self):
        for image in self.selected_image_list:
            self.user.removeImage(image)
        self.user.setup()
        self.selected_image_list.clear()
        self.refreshButtonIsClicked()
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListImages()
    apply_stylesheet(app, theme='dark_blue.xml', light_secondary = False)
    # apply_stylesheet(app, theme='dark_teal.xml', light_secondary = True)
    window.show()

    sys.exit(app.exec_())