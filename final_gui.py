"""
This class sets up the GUI that collects the user input 
The GUI shows what types of functions that can be viewed, and allows the user to select one of the functions
As soon as the user selects one of the options, a graph is plotted using default values
The user then enters the values of function parameters
As soon as the set button is clicked, a new graph is plotted with the desired parameters
The GUI also shows warning messages for invalid user inputs

If a new function is added, add a label describing it, add the item to the ComboBox, 
and add an elif statement in the select_graph function

To change the default values, go to setDefault() function

"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from polynomial import *
from trigFunctions import *
from sawtooth import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from exceptions import *

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__() #calling parent constructor
		self.setGeometry(50, 50, 500, 500) #(xpos, ypos, width, height)
		self.setWindowTitle("Graph viewer")
		self.initUI()
		self.setDefault()

	def initUI(self): #all the widgets that goes in the window are initialize here
		#Labels that explains the users the different types of functions as well as the action items
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
		self.sawLabel.setWordWrap(True) #The wordwrap allows to write multi-line texts
		
		self.rangeLabel = QtWidgets.QLabel(self)
		self.rangeLabel.setText("You can also choose the range of x values")
		self.rangeLabel.move(10,190)
		
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Choose a function from the drop down menu")
		self.label.move(90,220)

		#If a new function is added, add the function name to this ComboBox
		#Allows user to select of the predefined functions
		self.options=QComboBox(self) 
		self.options.addItem("Polynomial")
		self.options.addItem("Trig")
		self.options.addItem("Sawtooth")
		self.options.move(200,250)
		self.options.activated[str].connect(self.setDefault) #As soon as a function is selected, the parameters are set to default values
		self.options.activated[str].connect(self.select_graph) #Graph plotted with default values
		
		#Entry boxes 
		self.enterA = QLineEdit(self) 
		self.enterA.move(60,290)
		self.enterB = QLineEdit(self) 
		self.enterB.move(260,290)
		self.x_start = QLineEdit(self) 
		self.x_start.move(60,330)
		self.x_end = QLineEdit(self) 
		self.x_end.move(260,330)
		
		self.button=QPushButton("Set A, B, and the x range", self) #button for setting the parameter values
		self.button.move(150,380)
		self.button.clicked.connect(self.save_param)
		
		self.defaultLabel = QtWidgets.QLabel(self)
		self.defaultLabel.setText("The default values are A=1, B=1, and x goes from 0 to 5")
		self.defaultLabel.move(10,450)
		self.update()

	def setDefault(self):
		"""
		This method sets all parameters to default values and sets placeholder texts in the entry boxes
		Called at the start of the program, and when a new function is selected from the dropdown menu
		Default values can be changed here
		"""
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
	
	def update(self): 
		"""
		Resize all the labels so that they do not get cut off
		"""
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
		"""
		When the set button is clicked, this function connects all the entered values to the respective parameters
		Try catch blocks handles invalid user input
		"""
		try:
			#Throws emptyBoxError if one of the entry fields is empty
			#Throws ValueError if the value entered is not a number
			#Throws xRangeError if x_end value is not greater than x_start value
			
			if self.enterA.text() =="" or self.enterB.text() =="" or self.x_start.text() =="" or self.x_end.text() =="":
				raise emptyBoxError 
			
			if float(self.x_start.text())>= float(self.x_end.text()):
				print("X start:{}, x end:{}".format(self.x_start.text(), self.x_end.text()))
				raise xRangeError
			
			self.A= float(self.enterA.text())
			self.B= float(self.enterB.text())
			self.x_first = float(self.x_start.text())
			self.x_last = float(self.x_end.text())
			
			self.select_graph()
		
		except emptyBoxError:
			msg = QMessageBox()
			msg.setWindowTitle("Input Error")
			msg.setText("All entries need to be filled!")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()

		except ValueError:
			msg = QMessageBox()
			msg.setWindowTitle("Input Error")
			msg.setText("The inputs must only be numbers! Try again")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()

		except xRangeError:
			msg = QMessageBox()
			msg.setWindowTitle("Range Error")
			msg.setText("x end must be greater than x start")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()


	def select_graph(self):
		"""	
		Depending on the function selected from the ComboBox, 
		this method creates an object of the selected function and plots the graph
		"""
		if self.options.currentIndex()==0:
			graph=Polynomial(float(self.A), float(self.B), float(self.x_first), float(self.x_last))
		elif self.options.currentIndex()==1:
			graph=trig(float(self.A), float(self.B), float(self.x_first), float(self.x_last))
		else:
			graph=SawTooth(float(self.A), float(self.B), float(self.x_first), float(self.x_last))
		graph.plot_function()
		




