from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ButtonTabWidget import ButtonWidget
from re import search

class Log(QWidget):
    def __init__(self, filename = 'text.txt'):
        QWidget.__init__(self, None)
        self.layout = QVBoxLayout(self)
        
        self.label = QLabel('LOG VIEWER')
        # self.label.setStyleSheet('font-family: Optima; font-size: 16pt;')
        self.label.setStyleSheet('font-size: 16pt;')   
        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.label)
        self.row1.setAlignment(Qt.AlignLeft)

        self.label2 = QLabel('SEARCH')
        # self.label2.setStyleSheet('font-family: Optima; font-size: 16pt;')
        self.label2.setStyleSheet('font-size: 16pt;')   
        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.searching)
        self.row2 = QHBoxLayout()
        self.row2.setSpacing(55)
        self.row2.addWidget(self.label2)
        self.row2.addWidget(self.lineEdit)

        self.buttonTab = ButtonWidget(1)
        self.buttonTab.setupButtons(['copy'], ['#397D00'])
        self.buttonList = self.buttonTab.getButtonList()
        self.buttonList[0].clicked.connect(self.copyButtonIsClicked)
        
        self.logDisplay = QTextBrowser()  
        self.logDisplay.setStyleSheet('font-size: 14pt; font-weight: normal;')

        self.layout.addLayout(self.row1)
        self.layout.addLayout(self.row2)
        self.layout.addWidget(self.buttonTab)
        self.layout.addWidget(self.logDisplay)
        self.layout.setSpacing(15)
        self.layout.setAlignment(Qt.AlignTop)
        self.readFile(filename)
    
    # filename.txt
    def readFile(self, filename):
        file = open(filename, 'r') 
        self.lines = file.readlines() 
        file.close()

        file = open(filename, 'r') 
        whole_text = file.read()
        file.close()        
        self.logDisplay.setText(whole_text)
    
    def searching(self):
        keyword = self.lineEdit.text()
        display = ''

        for line in self.lines:
            if search(keyword.lower(), line.lower()):
                display += line
        self.logDisplay.setText(display)
    
    def copyButtonIsClicked(self):
        cb = QGuiApplication.clipboard()
        qString = self.logDisplay.toPlainText()

        cb.setText(str(qString))




