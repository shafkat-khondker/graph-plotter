"""
This program allows users to plot functions such as trigonometric functions, polynomial functions, as well as functions
with no simple mathematical representation, such as a SawTooth function. 
A GUI allows the user to select a function, and enter parameters such as Amplitude, Power, or frequency of a wave
The user can also adjust the range of the x values

The purpose of writing this program was to practice Object oriented progamming in Python.
"""
import sys 
from final_gui import * 

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_()) 
