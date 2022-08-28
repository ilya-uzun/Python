from PyQt5.Qt import *

class TabPage_SO(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.labelType = QLabel("№ типа", self)
        self.lineEditType = QLineEdit(self)
        self.lineEditType.setClearButtonEnabled(True)

        self.labelYearOfIssue = QLabel("Год выпуска *", self)
        self.spinBox = QSpinBox(self)
        self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(1917)
        self.spinBox.setMaximum(2060)
        self.spinBox.setProperty("value", 2020)

        self.labelSerialNumber = QLabel("Заводской №", self)
        self.lineEditSerialNumber = QLineEdit(self)
        self.lineEditSerialNumber.setClearButtonEnabled(True)

        self.labelSpecifications = QLabel("Характеристики", self)
        self.lineEditSpecifications = QLineEdit(self)
        self.lineEditSpecifications.setClearButtonEnabled(True)

        grid = QGridLayout(self)
        grid.addWidget(self.labelType, 0, 0)
        grid.addWidget(self.labelYearOfIssue, 0, 1)
        grid.addWidget(self.labelSerialNumber, 0, 2)
        grid.addWidget(self.lineEditType, 1, 0)
        grid.addWidget(self.spinBox, 1, 1)
        grid.addWidget(self.lineEditSerialNumber, 1, 2)
        grid.addWidget(self.labelSpecifications, 2, 0)
        grid.addWidget(self.lineEditSpecifications, 3, 0, 1, 3)
        grid.setRowStretch(4, 1)


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TabPage_SO(self), "Tab Zero")
        count = self.count()
        nb = QToolButton(text="Добавить", autoRaise=True)
        nb.clicked.connect(self.new_tab)
        self.insertTab(count, QWidget(), "")
        self.tabBar().setTabButton(count, QTabBar.RightSide, nb)

    def new_tab(self):
        index = self.count() - 1
        self.insertTab(index, TabPage_SO(self), "Tab %d" % index)
        self.setCurrentIndex(index)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.tabWidget = TabWidget()
        self.tableWidget = QTableWidget(0, 4)
        self.tableWidget.setHorizontalHeaderLabels(
            ["№ типа", "Год выпуска *", "Заводской №", "Характеристики"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)

        self.buttonAdd = QPushButton('Добавить из текущей вкладки в таблицу')
        self.buttonAdd.clicked.connect(self.addRowTable)
        self.buttonDel = QPushButton('Удалить выбранную строку в таблице')
        self.buttonDel.clicked.connect(self.delRowTable)

        vbox = QGridLayout(self.centralWidget)
        vbox.addWidget(self.tabWidget, 0, 0, 1, 2)
        vbox.addWidget(self.tableWidget, 1, 0, 1, 2)
        vbox.addWidget(self.buttonAdd, 2, 0)
        vbox.addWidget(self.buttonDel, 2, 1)

    def addRowTable(self):
        editType = self.tabWidget.currentWidget().lineEditType.text()
        spinYearOfIssue = str(self.tabWidget.currentWidget().spinBox.value())
        editSerialNumber = self.tabWidget.currentWidget().lineEditSerialNumber.text()
        editSpecifications = self.tabWidget.currentWidget().lineEditSpecifications.text()

        if not editType or not editSerialNumber or not editSpecifications:
            msg = QMessageBox.information(self, 'Внимание', 'Заполните все поля!')
            return
        self.tableWidget.setSortingEnabled(False)
        rows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rows)
        self.tableWidget.setItem(rows, 0, QTableWidgetItem(editType))
        self.tableWidget.setItem(rows, 1, QTableWidgetItem(spinYearOfIssue))
        self.tableWidget.setItem(rows, 2, QTableWidgetItem(editSerialNumber))
        self.tableWidget.setItem(rows, 3, QTableWidgetItem(editSpecifications))
        self.tableWidget.setSortingEnabled(True)
        # print(editType, spinYearOfIssue, editSerialNumber, editSpecifications)

    def delRowTable(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            msg = QMessageBox.information(self, 'Внимание', 'Выберите строку для удаления')
            return
        self.tableWidget.removeRow(row)


qss = """
QLabel {
    font: 8pt "MS Shell Dlg 2";
}
QLineEdit {
    font: 12pt "Calibri";
}
QSpinBox {
    font: 12pt "Calibri";
}
"""

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyleSheet(qss)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())