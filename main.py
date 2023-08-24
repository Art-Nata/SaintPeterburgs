import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class DrawCircle(QMainWindow):
    def __init__(self):
        super(DrawCircle, self).__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.w = self.size().width()
        self.h = self.size().height()
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.paint(qp)
            qp.end()

    def run(self):
        self.flag = True
        self.update()

    def paint(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = randint(10, 80)
        x = randint(10, self.w - a)
        y = randint(10, self.h - a)

        qp.drawEllipse(x, y, a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.except_hook = except_hook
    app = QApplication(sys.argv)
    wnd = DrawCircle()
    wnd.show()
    sys.exit(app.exec())

