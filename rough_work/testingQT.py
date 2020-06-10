from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__() #calling parent constructor
		self.setGeometry(500, 500, 700, 300) #(xpos, ypos, width, height)
		self.setWindowTitle("You got this Shups")
		self.initUI()

	def initUI(self): #all the stuff that goes in the window goes here
		self.label = QtWidgets.QLabel(self)
		self.label.setText("my first label")
		self.label.move(50,50)

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Click me")
		#self.b1.move(50,50)
		self.b1.clicked.connect(self.clicked2) #connects this button to the event function	

	def clicked2(self):
		self.label.setText("You pressed the button")
		self.update()

	def update(self): #resize the label so that it doesn't get cut off
		self.label.adjustSize()


def window():
	app = QApplication(sys.argv)
	win = MyWindow()

	win.show()
	sys.exit(app.exec_()) #close this

window()

