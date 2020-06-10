#from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import *
import sys 
from final_gui import * 

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_()) 
