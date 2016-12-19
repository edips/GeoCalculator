from PyQt4 import QtCore, QtGui
from calculatorUi import Ui_hesap
import sys

class Calculator(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_hesap()
        self.ui.setupUi(self)

        # Validations
        v = QtGui.QDoubleValidator()
        v.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.a.setValidator(v)
        self.ui.b.setValidator(v)
        # Signal/slot connections.
        self.setupConnections()

    def sum(self):
        a1 = float(self.ui.a_to1.text())
        b1 = float(self.ui.b_to1.text())
        c1 = a1 + b1
        C1 = str(c1)
        self.ui.c.setText(str(C1))

    def setupConnections(self):
        self.connect(self.ui.calculate, QtCore.SIGNAL('clicked()'), self.sum)

'''if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)  
  window = Calculator()
  window.show()
  sys.exit(app.exec_())'''
