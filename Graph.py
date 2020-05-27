from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure
import os
import numpy as np
import random


class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        # self.canvas.setFixedSize(400, 500)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        # widget = NavigationToolbar(self.canvas, self)
        # widget.setStyleSheet("background-color: White;")
        # vertical_layout.addWidget(widget)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        self.setMaximumSize(200,400)



class Graph(QWidget):

    def __init__(self, title, x_list, y_list):
        QWidget.__init__(self)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'ui')
        self.path = path
        self.ui_path = self.path + '/graph.ui'
        designer_file = QFile(self.ui_path)
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        loader.registerCustomWidget(MplWidget)
        self.ui = loader.load(designer_file, self)
        designer_file.close()

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)

    

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(x_list, y_list)
        
        self.ui.MplWidget.canvas.axes.set_title(title)
        self.ui.MplWidget.canvas.draw()

