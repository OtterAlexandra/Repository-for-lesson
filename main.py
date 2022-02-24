from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint

import sys


class Test(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.btn.clicked.connect(self.circle)
        self.start = False

    def circle(self):
        self.start = True
        self.update()

    def paintEvent(self, event):
        if self.start:
            x, y = [randint(10, 400) for _ in range(2)]
            rad = randint(10, 400)

            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            painter.drawEllipse(x, y, rad, rad)

            painter.end()
            self.start = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
