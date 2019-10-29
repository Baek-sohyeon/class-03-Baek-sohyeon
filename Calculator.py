from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from keypad2 import operatorList, constantList, functionList
import calcFunctions

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        #숫자버튼 생성하기
        for i in range(0,10):
            self.digitButton[i] = Button(str(i), self.buttonClicked)

        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()
        numLayout = QGridLayout()

        buttonGroups = {
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }


        # Operator Buttons, Function Buttons, Constant Buttons
        for label in buttonGroups.keys():
            r = 0
            c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # 숫자버튼 배열하기(버튼 0은 따로 처리함)
        for i in range(1, 10):
            numLayout.addWidget(self.digitButton[i], (8 - (i - 1)) / 3, (i - 1) % 3)

        numLayout.addWidget(self.digitButton[0], 3, 0)

        # . and = Buttons (따로 처리해줌)
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)
        # '.' , '='
        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        calculator = ['3.141592','3E+8','340','1.5E+8']
        func = [calcFunctions.factorial, calcFunctions.decToBin, calcFunctions.binToDec, calcFunctions.decToBin, calcFunctions.decToRoman]
        try:

            if self.display.text() == 'Error!':
                self.display.setText('')

            button = self.sender()
            key = button.text()

            if key == '=':
                result = str(eval(self.display.text()))
                # 부동소수를 처리해준 값을 리턴해줍니다!
                self.display.setText(calcFunctions.floatPoint(result))

            elif key == 'C':
                self.display.setText('')


            elif key in constantList:
                for i in range(len(constantList)):
                    if key == constantList[i]:
                        self.display.setText(self.display.text() + calculator[i])


            elif key in functionList:
                for i in range(len(functionList)):
                    if key == functionList[i]:
                        n = self.display.text()
                        value = func[i](n)
                        self.display.setText(str(value))

            else:
                self.display.setText(self.display.text() + key)


        except:
            pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
