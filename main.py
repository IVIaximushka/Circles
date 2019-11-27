import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Form')

        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(50, 50)
        self.btn.move(0, 0)
        self.n = 0
        self.btn.clicked.connect(self.run)

    def run(self):
        self.r, self.g, self.b = (random.randint(0, 255), random.randint(0, 255),
                                  random.randint(0, 255))
        self.x, self.y, self.h = (random.randint(0, 250), random.randint(0, 250),
                                  random.randint(0, 50))
        self.n = 1
        self.update()

    def paintEvent(self, event):
        if self.n != 0:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(self.r, self.g, self.b))
            qp.drawEllipse(self.x, self.y, self.h, self.h)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
