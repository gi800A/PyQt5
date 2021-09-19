# prova prima app using pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont


#calsses 
class main_root(QWidget): # ereditarietà
#costruttoree:
	def __init__(self):
		super().__init__()
		
	
	def root_window_init(self):
		self.setWindowTitle("800A Forte")
		self.resize(300, 300)
		self.move(300, 220)
		# you can use this method: root.setGeometry(300, 300, 300, 220)	
		self.setWindowIcon(QIcon('mole.png'))
		self.show()


# M A I N:

#entry point GUI
app = QApplication(sys.argv)

#create an object 
root = main_root()
root.root_window_init()


sys.exit(app.exec_())

