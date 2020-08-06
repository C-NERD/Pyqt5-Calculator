from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

app = QApplication([])
size = app.primaryScreen().size()

width = 280
height = 300

w1 = 0
h1 = height-((height-(1/3*(height)))/4)
w2 = width/4
h2 = height-(2*(height-(1/3*(height)))/4)
w3 = (2*(width/4))
h3 = height-(3*(height-(1/3*(height)))/4)
w4 = (3*(width/4))
h4 = height-(4*(height-(1/3*(height)))/4)
w = 0
h = 0
con = True
screen = ''

class main(QMainWindow):
    def __init__(self):
        super().__init__()

        #global w
        #global h
        
        self.setGeometry(500, 250, width, height)
        self.setWindowTitle('Tube_cal')
        self.setWindowIcon(QIcon("back000.png"))

        self.text = QLineEdit(self)
        self.text.setReadOnly(True)
        self.text.setAlignment(Qt.AlignRight)
        self.text.resize(width, (1/3*(height)))
        self.text.move(0, 0)

        btn = ['0','1','2','3','4','5','6','7','8','9','.','=','+','/','x','-']
        for n in btn:
            if n=='0':
                w = w1
                h = h1
                command = self.num
            if n=='.':
                w = w2
                h = h1
                command = self.point
            if n=='=':
                w = w3
                h = h1
                command = self.Equal
            if n=='+':
                w = w4
                h = h1
                command = self.sym
            if n=='1':
                w = w1
                h = h2
                command = self.num
            if n=='2':
                w = w2
                h = h2
                command = self.num
            if n=='3':
                w = w3
                h = h2
                command = self.num
            if n=='-':
                w = w4
                h = h2
                command = self.sym
            if n=='4':
                w =w1
                h = h3
                command = self.num
            if n=='5':
                w = w2
                h = h3
                command = self.num
            if n=='6':
                w = w3
                h = h3
                command = self.num
            if n=='x':
                w = w4
                h = h3
                command = self.sym
            if n=='7':
                w = w1
                h = h4
                command = self.num
            if n =='8':
                w = w2
                h = h4
                command = self.num
            if n=='9':
                w = w3
                h = h4
                command = self.num
            if n=='/':
                w = w4
                h = h4
                command = self.sym
                
            button = QPushButton(n, self)
            button.resize(width/4, (height-(1/3*(height)))/4)
            button.move(w, h)
            button.clicked.connect(command)

        action1 = QAction('clear', self)
        action1.triggered.connect(self.clear)

        action2 = QAction('del', self)
        action2.triggered.connect(self.delete)
            
        cleared = self.addToolBar('clear')
        cleared.addAction(action1)

        deleted = self.addToolBar('del')
        deleted.addAction(action2)
            
        self.show()
        
    def num(self):
        global con
        global screen

        sender = self.sender()
        number = str(sender.text())

        if con==False:
            self.text.setText(number)
            con = True
            
        else:
            self.text.setText(self.text.text() + number)

    def sym(self):
        global con
        global screen

        sender = self.sender()
        symbol = str(sender.text())

        screen = (self.text.text())

        if len(screen.split())>=3:
            con = False

        elif con == True:
            self.text.setText(self.text.text() + ' ' + symbol + ' ')

    def point(self):
        global con
        if con==True:
            self.text.setText(self.text.text() + '.')

    def clear(self):
        self.text.clear()
            
    def delete(self):
        self.text.backspace()

    def Equal(self):
        global con
        global screen

        equal = (self.text.text()).split()

        if len(equal) >= 3:
            con = False

        if con == False:
            if equal[1] == '+':
                result = float(equal[0]) + float(equal[2])
                self.text.setText(str(result))

            elif equal[1] == '-':
                result = float(equal[0]) - float(equal[2])
                self.text.setText(str(result))

            elif equal[1] == 'x':
                result = float(equal[0]) * float(equal[2])
                self.text.setText(str(result))

            elif equal[1] == '/':
                result = float(equal[0]) / float(equal[2])
                self.text.setText(str(result))

        con = True

   
if __name__ == '__main__':
    
    app.setStyleSheet('QPushButton {background-color:black; color:white; font-size: 30px} QPushButton:hover {background-color:#ddd} QLineEdit {font-size:30px;}')
    ex = main()
    app.exec_()
