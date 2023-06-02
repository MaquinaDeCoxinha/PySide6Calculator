from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QTextEdit
from info import Info
from mainwindow import MainWindow
from display import Display
import sys, os
from PySide6.QtGui import QIcon
from styles import setupTheme
from variables import WINDOW_ICON_PATH
from buttons import ButtonGrid, Button
if __name__ == "__main__":
    app = QApplication()

    setupTheme()

    window = MainWindow()
    icon = QIcon(str(WINDOW_ICON_PATH))

    info = Info()
    info.setText('Sua Conta')
    window.addWidgetToVLayout(info)    

    display = Display()
    window.addWidgetToVLayout(display)
    Buttons = ButtonGrid(displayArg=display, infoArg=info)
    Buttons.createButtons(window)
    #Buttons.createButtons.key.clicked.connect(Buttons._insertButtonTextToDisplay())

    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.adjustWidgetSize()
    window.show()
    app.exec()