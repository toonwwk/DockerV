import os
import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from pyside_material import apply_stylesheet

class ImagePlayer(QWidget):
    def __init__(self, filename):
        QWidget.__init__(self, None)

        # Load the file into a QMovie
        self.movie = QMovie(filename, QByteArray(), self)

        size = self.movie.scaledSize()
        self.setGeometry(0, 0, size.width(), size.height())


        self.movie_screen = QLabel()
        # Make label fit the gif
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.movie_screen.setAlignment(Qt.AlignCenter)

        # Create the layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)

        self.setLayout(main_layout)

        # Add the QMovie object to the label
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie.loopCount()
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir)
    image_path = path + "\images\docker_gif3.gif"
    gif = image_path
    app = QApplication(sys.argv)
    player = ImagePlayer(gif)
    player.show()
    sys.exit(app.exec_())
