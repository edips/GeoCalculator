import sys

from PySide import QtGui

from sum import Calculator


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  window = Calculator()
  window.show()
  sys.exit(app.exec_())
