from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QGridLayout, QPushButton, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from variables import BUTTON_SIZE
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Calculadora")

        self.cw = QWidget() #cw = central_widget
        self.gridLayout = QGridLayout()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.vLayout.addLayout(self.gridLayout)
        self.setCentralWidget(self.cw)

    def adjustWidgetSize(self): 
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget):
        self.vLayout.addWidget(widget)
