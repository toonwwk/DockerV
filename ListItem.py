import sys
from PySide2 import QtWidgets, QtGui
from PySide2 import QtCore
from PySide2 import QtUiTools
from pyside_material import apply_stylesheet
from ClickableLabel import ClickableLabel


class ContainerListItem(QtWidgets.QWidget):
    def __init__(self, c_name, i_name, ip,  owner, id, status, is_header=False, ports=[]):
        super(ContainerListItem, self).__init__()
        self.check_box = QtWidgets.QCheckBox()
        if is_header:
            layout = QtWidgets.QHBoxLayout(self)
            temp = QtWidgets.QLabel('')
            temp.setFixedSize(40, 50)
            name  = QtWidgets.QLabel('Name')
            status = QtWidgets.QLabel('Status')
            status.setFixedSize(70,50)
            name.setMinimumSize(150,50)
            image_name = QtWidgets.QLabel('Image name')
            image_name.setMinimumSize(150, 50)
            ip = QtWidgets.QLabel('Ip')
            ip.setMinimumSize(100, 50)
            ports = QtWidgets.QLabel("Port")
            ports.setMinimumSize(140, 50)
            owner = QtWidgets.QLabel('Owner')
            owner.setMinimumSize(70,50)
            layout.addWidget(temp)
            layout.addWidget(status)
            layout.addWidget(name)
            layout.addWidget(image_name)
            layout.addWidget(ip)
            layout.addWidget(ports)
            layout.setSpacing(30)
            layout.addWidget(owner)

        else:
            self.check_box.setFixedSize(40, 50)
            self.container_name = ClickableLabel(c_name)
            self.container_name.setMinimumSize(150, 50)
            self.image_name = ClickableLabel(i_name)
            self.image_name.setMinimumSize(150, 50)
            self.ip = QtWidgets.QLabel(ip)
            self.ip.setMinimumSize(100, 50)
            self.ports = QtWidgets.QPushButton("9000:9000")
            self.ports.setMinimumSize(140, 50)
            self.ports.setFlat(True)
            self.ownerships = QtWidgets.QLabel(owner)
            self.ownerships.setMinimumSize(70,50)
            self.id = id
            self.status_button = QtWidgets.QPushButton(status)
            self.status_button.setFixedSize(70,50)
            self.status_button.setFlat(True)
            self.set_ui()
            self.status_button.setTabletTracking(False)

    def set_ui(self):
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.check_box)
        layout.addWidget(self.status_button)
        layout.addWidget(self.container_name)
        layout.addWidget(self.image_name)
        layout.addWidget(self.ip)
        layout.addWidget(self.ports)
        layout.addWidget(self.ownerships)
        layout.setSpacing(30)
        layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.setLayout(layout)
        self.show()

    def getCheckBox(self):
        return self.check_box

    def tick_handler(self):
        self.ContainerIdSignal.emit(5, self.id)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.widget = ContainerListItem(
            "alpine", "q12", "120.10.1.1", "baypc", "1", "exited", True)

        self.setWindowTitle("DockerV")

        self.setCentralWidget(self.widget)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_pink.xml')
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
