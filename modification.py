from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from random import randint
from Ui import Ui_Form

import sys


class Test(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            pen = QPen()
            pen.setWidth(8)
            color = QColor(*[randint(0, 255) for _ in range(3)])
            pen.setColor(color)
            painter.setPen(pen)
            painter.drawEllipse(x, y, rad, rad)

            painter.end()
            self.start = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())

