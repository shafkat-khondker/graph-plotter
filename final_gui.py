from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from polynomial import *
from trigFunctions import *
from sawtooth import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from exceptions import *
#MyWindow, self
class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__() #calling parent constructor
		#default parameters
		self.setGeometry(50, 50, 500, 500) #(xpos, ypos, width, height)
		self.setWindowTitle("Graph viewer")
		self.initUI()
		self.setDefault()

	def initUI(self): #all the stuff that goes in the window goes here
		self.welcomeLabel = QtWidgets.QLabel(self)
		self.welcomeLabel.setText("Welcome to the Graph viewer!")
		self.welcomeLabel.move(10,10)

		self.topLabel = QtWidgets.QLabel(self)
		self.topLabel.setText("You can plot any of the following types of functions")
		self.topLabel.move(10,40)

		self.polyLabel = QtWidgets.QLabel(self)
		self.polyLabel.setText("1: Polynomial function in the form y= A*(x)^B. ")
		self.polyLabel.move(10,70)

		self.trigLabel = QtWidgets.QLabel(self)
		self.trigLabel.setText("2: Trig function in the form y= A*sin(B*x). ")
		self.trigLabel.move(10,100)
		
		self.sawLabel = QtWidgets.QLabel(self)
		self.sawLabel.setText("3: SawTooth function where A is amplitude and B is vertical shift. The function has an upward slope of 1 and downward slope of -0.5")
		self.sawLabel.setGeometry(10,130,480,60)
		self.sawLabel.setWordWrap(True)
		#self.sawLabel.move(10,130)

		self.rangeLabel = QtWidgets.QLabel(self)
		self.rangeLabel.setText("You can also choose the range of x values")
		self.rangeLabel.move(10,190)

		self.label = QtWidgets.QLabel(self)
		self.label.setText("Choose a function from the drop down menu")
		self.label.move(90,220)

		self.options=QComboBox(self)
		self.options.addItem("Polynomial")
		self.options.addItem("Trig")
		self.options.addItem("Sawtooth")
		self.options.move(200,250)
		self.options.activated[str].connect(self.setDefault)
		self.options.activated[str].connect(self.select_graph) 
		 
		self.enterA = QLineEdit(self)
		self.enterA.move(60,290)
		
		self.enterB = QLineEdit(self)
		self.enterB.move(260,290)

		self.x_start = QLineEdit(self)
		self.x_start.move(60,330)
		
		self.x_end = QLineEdit(self)
		self.x_end.move(260,330)
		
		self.button=QPushButton("Set A, B, and the x range", self)
		self.button.move(150,380)
		self.button.clicked.connect(self.save_param)
		self.options.activated[str].connect(self.setDefault) 
		self.defaultLabel = QtWidgets.QLabel(self)
		self.defaultLabel.setText("The default values are A=1, B=1, and x goes from 0 to 5")
		self.defaultLabel.move(10,450)
		self.update()

	def setDefault(self):
		self.A=1
		self.B=1
		self.x_first=0
		self.x_last=5
		self.enterA.clear()
		self.enterB.clear()
		self.x_start.clear()
		self.x_end.clear()
		self.enterA.setPlaceholderText("Enter value for A")
		self.enterB.setPlaceholderText("Enter value for B")
		self.x_start.setPlaceholderText("Enter x start value")
		self.x_end.setPlaceholderText("Enter x end value")
	
	def update(self): #resize the label so that it doesn't get cut off
		self.enterA.adjustSize()
		self.enterB.adjustSize()
		self.button.adjustSize()
		
		self.x_start.adjustSize()
		self.x_end.adjustSize()
		self.label.adjustSize()
		self.welcomeLabel.adjustSize()
		self.topLabel.adjustSize()
		self.polyLabel.adjustSize()
		self.trigLabel.adjustSize()
		self.options.adjustSize()
		self.rangeLabel.adjustSize()
		self.defaultLabel.adjustSize()

	def save_param(self):
		try:
			float(self.enterA.text())
			float(self.enterB.text())
			float(self.x_start.text())
			float(self.x_end.text())

			self.A=self.enterA.text()
			self.B=self.enterB.text()
			#print("Value of A is {} and B is {}".format(self.A, self.B))
			self.x_first = self.x_start.text()
			self.x_last = self.x_end.text()
			#print("Value of x start is {} and x end is {}".format(self.x_first,self.x_last))
			if self.x_first>=self.x_last:
				raise xRangeError
			self.select_graph()
		
		except ValueError:
			msg = QMessageBox()
			msg.setWindowTitle("Input Error")
			msg.setText("The inputs must only be numbers! Try again")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()

		except xRangeError:
			msg2 = QMessageBox()
			msg2.setWindowTitle("Range Error")
			msg2.setText("x end must be greater than x start")
			msg2.setIcon(QMessageBox.Information)
			msg2.exec_()


	def select_graph(self):
		if self.options.currentIndex()==0:
			graph=Polynomial(float(self.A), float(self.B), float(self.x_first), float(self.x_last))
		elif self.options.currentIndex()==1:
			graph=trig(float(self.A), float(self.B), float(self.x_first), float(self.x_last))
		else:
			graph=SawTooth(float(self.A), float(self.B), float(self.x_first), float(self.x_last))
		graph.plot_function()
		




