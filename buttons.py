from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLineEdit, QTextEdit, QPushButton
from mainwindow import MainWindow
from PySide6.QtCore import Slot
from variables import BUTTON_SIZE, MED_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber, Calculate


class Button(QPushButton):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MED_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(BUTTON_SIZE,BUTTON_SIZE)

class ButtonGrid(QGridLayout):
    def __init__(self,displayArg,infoArg,*args,**kwargs):
          super().__init__(*args,**kwargs)
          self.display = displayArg
          self.info = infoArg
          self.number1 = None
          self.number2 = None
          self.oprEscolhido = None
          self.result = None
    def createButtons(self, window):
        self.buttonsMap = {}
        keyBoard = [
            ["C","**","%","+"],
            ["7","8","9","-"],
            ["4","5","6","*"],
            ["1","2","3","/"],
            ["","0",".","="]
        ]
        for row, keys in enumerate(keyBoard):
            for col, keyText in enumerate(keys):
                key = Button(keyText)
                if not isNumOrDot(keyText) and not isEmpty(keyText):
                    key.setProperty('cssClass', 'specialButton')
                self.addWidget(key, row, col)
        #key.clicked.connect(self._insertButtonTextToDisplay)
                keySlot = self._makeKeyDisplaySlot(
                    self._insertKeyTextToDisplay,key
                )
                key.clicked.connect(keySlot)  # type: ignore
                window.vLayout.addLayout(self)
    def _makeKeyDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
    def _updatePartialInfo(self, num1, opr):
        self.info.setText(f'{num1} {opr} ??')
    def _updateInfo(self, num1, num2, opr, result):
        self.info.setText(f'{num1} {opr} {num2} = {result}')
    def _whatToDoWithIt(self, key):
        key_text = key.text()
        if key_text in '+-*/**%': #tecla de operacao apertada
            if self.number1 is None and key_text != self.oprEscolhido: #se nao há um numero 1
                self.number1 = self.display.text()
                self.number2 = None
                self.display.clear()
                self.oprEscolhido = key_text
                self._updatePartialInfo(self.number1, self.oprEscolhido)
            elif self.result is not None and self.display.text() == '':
                self.number1 = self.result
                self.number2 = None
                self.result = None
                self.oprEscolhido = key_text
                self._updatePartialInfo(self.number1, self.oprEscolhido)
            else:
                self.number2 = self.display.text()
                self.result = Calculate(self.number1, self.number2, self.oprEscolhido)
                self.display.clear()
                self._updateInfo(self.number1, self.number2, self.oprEscolhido, self.result)
                #self.number1 = str(result)
                #self.oprEscolhido = key_text
        elif key_text == 'C':
            self.display.clear()
            self.number1 = None
            self.number2 = None
            self.oprEscolhido = None
            self.result = None
            self.info.setText('Sua Conta')
        elif key_text == '=':
            if self.display.text() == '' and self.result != None: #repetindo operações
                self.number1 = self.result
                self.result = Calculate(self.number1, self.number2, self.oprEscolhido)
                self._updateInfo(self.number1, self.number2, self.oprEscolhido, self.result)
            elif self.number1 is not None and self.oprEscolhido is not None: #normal operation
                self.number2 = self.display.text()
                self.result = Calculate(self.number1, self.number2, self.oprEscolhido)
                self.display.clear()
                self._updateInfo(self.number1, self.number2, self.oprEscolhido, self.result)
            else: #in case if there is nothing to calculate
                return
        else:
            print('voce deve ter apertado .')
            return
        
    def _insertKeyTextToDisplay(self, key):
        key_text = key.text()
        newDisplayValue = self.display.text() + key_text
        if not isValidNumber(newDisplayValue):
            self._whatToDoWithIt(key)
            return
        self.display.insert(key_text)
        print('botao apertado')
    #def _saveNumberAndInsertToLabel(self, )
    
