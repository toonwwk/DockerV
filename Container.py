from pyside_material import apply_stylesheet
from PySide2 import QtWidgets, QtGui, QtCore
from ListItem import ContainerListItem
from Connection import Connection
from ButtonTabWidget import ButtonWidget
from Popup import Popup, CreateContainerForm
import sys
import docker
import time


class CustomListHead(QtWidgets.QWidget):
    def __init__(self):
        super(CustomListHead, self).__init__()
        self.project_title = QtWidgets.QLabel("Today")
        self.set_ui()

    def set_ui(self):
        self.show()

# -----------------------------------


class ListWidget(QtWidgets.QListWidget):
    def __init__(self):
        super(ListWidget, self).__init__()
        self.ListHead = CustomListHead()
        self.container_list = []
        self.set_ui()
        self.checkbox_dict = {}
        self.selected_container = []

    def set_ui(self):
        self.update(self.ListHead)
        pass

    def UpdateList(self, containers):
        self.container_list = []
        self.clear()
        for c in containers:
            ListItem = ContainerListItem(
                c.image.short_id, c.attrs["Config"]["Image"], c.attrs["Platform"], "Local Admin", c.id, c.status)
            self.container_list.append(c.id)
            self.addCustomItem(ListItem)
            ListItem.check_box.stateChanged.connect(
                lambda state, c=ListItem.check_box, id=ListItem.id: (self.checkboxIsPressed(c, id)))
            self.checkbox_dict[c.id] = False

    def addCustomItem(self, widget):
        self.update(widget)

    def update(self, widget):
        item = QtWidgets.QListWidgetItem(self)
        item.setFlags(QtCore.Qt.NoItemFlags)
        item.setSizeHint(QtCore.QSize(40, 80))
        self.addItem(item)
        self.setItemWidget(item, widget)

    def checkboxIsPressed(self, cb, id):
        self.checkbox_dict[id] = not self.checkbox_dict[id]


class Container(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, None)
        self.list_widget = ListWidget()
        self.button_array = ButtonWidget(8)
        titles = ["start", "stop", "kill",
                  "restart", "pause", "unpause", "remove", "Create +"]
        colors = ["green", "red", "red", "blue",
                  "blue", "blue", "red", "black"]
        func = [self.startContainers, self.stopContainers, self.killContainers, self.restartContainers,
                self.pauseContainers, self.unpauseContainers, self.removeContainers, self.createContainer]
        self.button_array.setupButtons(titles, colors, func)
        self.set_ui()

    def set_ui(self):
        self.c = Connection()
        lst = self.c.getContainersDetail()
        self.list_widget.UpdateList(lst)
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.addWidget(self.button_array)
        vertical_layout.addWidget(self.list_widget)
        self.setLayout(vertical_layout)
        self.show()

    def startContainers(self):
        for container in self.c.getContainersDetail():
            if self.list_widget.checkbox_dict[container.id]:
                container.start()
                print("starting", container)
        time.sleep(5)
        self.list_widget.UpdateList(self.c.getContainersDetail())

    def stopContainers(self):
        for container in self.c.getContainersDetail():
            if self.list_widget.checkbox_dict[container.id]:
                container.stop()
                print("stop", container)

        time.sleep(5)
        self.list_widget.UpdateList(self.c.getContainersDetail())

    def killContainers(self):
        for container in self.c.getContainersDetail():
            if self.list_widget.checkbox_dict[container.id]:
                try:
                    container.kill()
                    print("kill", container)
                except docker.errors.APIError as e:
                    print(e)
                    p = Popup(e)
        time.sleep(5)
        self.list_widget.UpdateList(self.c.getContainersDetail())

    def restartContainers(self):
        for container in self.c.getContainersDetail():
            if self.list_widget.checkbox_dict[container.id]:
                try:
                    container.restart()
                    print("restart", container)
                except docker.errors.APIError as e:
                    print(e)
                    p = Popup(e)
        time.sleep(5)
        self.list_widget.UpdateList(self.c.getContainersDetail())

    def pauseContainers(self):
        for container in self.c.getContainersDetail():
            if self.list_widget.checkbox_dict[container.id]:
                try:
                    container.pause()
                    print("pause", container)
                except docker.errors.APIError as e:
                    print(e)
                    p = Popup(e)
        time.sleep(5)
        self.list_widget.UpdateList(self.c.getContainersDetail())

    def unpauseContainers(self):
        for container in self.c.getContainersDetail():
            if self.list_widget.checkbox_dict[container.id]:
                try:
                    container.unpause()
                    print("unpause", container)
                except docker.errors.APIError as e:
                    print(e)
                    p = Popup(e)
        time.sleep(5)
        self.list_widget.UpdateList(self.c.getContainersDetail())

    def removeContainers(self):
        for container in self.c.getContainersDetail():
            if self.list_widget.checkbox_dict[container.id]:
                try:
                    container.remove()
                    print("remove", container)
                except docker.errors.APIError as e:
                    print(e)
                    p = Popup(e)
        time.sleep(5)
        self.list_widget.UpdateList(self.c.getContainersDetail())

    def createContainer(self, widget):
        form = CreateContainerForm()
        b = form.getOk()
        print(b)
        b.clicked.connect(self.createContainerHandler)

    def createContainerHandler(self):
        print("hello")
        # print(widget.nameEdit.displayText)


class MainWindowUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.set_ui()

    def set_ui(self):
        apply_stylesheet(app, theme='dark_pink.xml')
        vertical_layout = QtWidgets.QVBoxLayout()
        widget = Container()
        widget.setLayout(vertical_layout)
        self.setCentralWidget(widget)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindowUI()
    sys.exit(app.exec_())
