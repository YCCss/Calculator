#简易的计算器制作
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from calculator import Ui_MainWindow

class Calcu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.png'))
        self.setupUi(self)
        self.connection()
        self.show()
    
    def num_0(self):
        self.lineEdit.insert('0')
    
    def num_1(self):
        self.lineEdit.insert('1')
        
    def num_2(self):
        self.lineEdit.insert('2')
        
    def num_3(self):
        self.lineEdit.insert('3')
        
    def num_4(self):
        self.lineEdit.insert('4')
        
    def num_5(self):
        self.lineEdit.insert('5')
        
    def num_6(self):
        self.lineEdit.insert('6')
        
    def num_7(self):
        self.lineEdit.insert('7')
        
    def num_8(self):
        self.lineEdit.insert('8')
    
    def num_9(self):
        self.lineEdit.insert('9')
    
    def op_plus(self):
        self.lineEdit.insert('+')
        
    def op_minus(self):
        self.lineEdit.insert('-')
        
    def op_multiply(self):
        self.lineEdit.insert('*')
    
    def op_divide(self):
        self.lineEdit.insert('/')
    
    def op_ce(self):
        self.lineEdit.clear()
        
    def calculate(self):
        text = self.lineEdit.text()
        try:
            self.lineEdit.setText(str(eval(text)))
        except:
            self.lineEdit.setText('Error!')
        
    def connection(self):
        self.Num_0.clicked.connect(self.num_0)
        self.Num_1.clicked.connect(self.num_1)
        self.Num_2.clicked.connect(self.num_2)
        self.Num_3.clicked.connect(self.num_3)
        self.Num_4.clicked.connect(self.num_4)
        self.Num_5.clicked.connect(self.num_5)
        self.Num_6.clicked.connect(self.num_6)
        self.Num_7.clicked.connect(self.num_7)
        self.Num_8.clicked.connect(self.num_8)
        self.Num_9.clicked.connect(self.num_9)
        self.OP_plus.clicked.connect(self.op_plus)
        self.OP_minus.clicked.connect(self.op_minus)
        self.OP_multiply.clicked.connect(self.op_multiply)
        self.OP_divide.clicked.connect(self.op_divide)
        self.OP_CE.clicked.connect(self.op_ce)
        self.OP_equal.clicked.connect(self.calculate)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ca = Calcu()
    sys.exit(app.exec_())
