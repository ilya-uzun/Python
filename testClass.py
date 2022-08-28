# Связь между классами

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow


# parent class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 366)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect.setGeometry(QtCore.QRect(440, 250, 101, 41))


# child class
class Terminal(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

    def add_function(self):
        self.btn_connect.clicked.connect(self.start)

    def start(self):
        print('!!!!')


class MainWindow(QMainWindow, Terminal):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.add_function()


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    app.exec()