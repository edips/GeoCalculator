import sys

from PySide import QtGui

from surveyhesap import hesap


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
    #QCleanlooksStyle
  #app.setStyle('Oxygen')
  #app.setStyle('Windows')
  #app.setStyle("cleanlooks")
  #app.setStyle("plastique")
  #app.setStyle('GTK')
  #app.setStyle('Motif')
  #app.setStyle('CDE')
  
  window = hesap()
  window.show()
  sys.exit(app.exec_())
