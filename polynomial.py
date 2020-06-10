"""
This class allows the user to plot simple polynomial functions in the form of y=A*(x)^B
Functions such as square roots are also supported
"""
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction 
from function import *

class Polynomial(Function):
	def __init__(self, A, B, x_start, x_end):
		super().__init__(A, B, x_start, x_end)

	def x_range(self):
		#for powers (B values) that have an even denominator, (eg square roots), the negative x values need to be truncated
		if (Fraction(self.B).limit_denominator().denominator % 2 == 0) and self.x_start<0:
			self.x_start=0
		x_range = np.arange(self.x_start, self.x_end, 0.01)	
		if self.B>0:
			return x_range
		else:
			#if the power is negative, the 0 value needs to be removed from the array to avoid DividebyZero exception
			index=0
			for i in range(len(x_range)):
				if abs(x_range[i]) < 0.0001:
					index = i
					return np.delete(x_range, index)
			return x_range
	
	def y_values(self, x):
		fx=np.zeros(len(x))
		for i in range(len(x)):
			#The following needs to be done because python cannot raise negative values to decimals 
			#that have an odd denominator. eg (-1)^0.2 or (-1)^-0.2 will not work 
			if Fraction(self.B).limit_denominator().denominator % 2 == 0 or Fraction(self.B).limit_denominator().denominator == 1 :
				fx[i]=self.A*(x[i])**self.B 
			else:
				fx[i]=self.A*(np.sign(x[i])*(np.abs(x[i]))**self.B)	
		return fx

	def plot_function(self):
		plt.close()
		plt.ion()
		plt.gcf().canvas.set_window_title('Polynomial function')
		plt.title("y=A*x^B, where A = {}, and B ={}".format(self.A, self.B))
		x = self.x_range()
		y = self.y_values(x)
		plt.ylim(np.amin(y)-1, np.amax(y)+1)
		plt.plot(x, y)
		plt.xlabel("x values")
		plt.ylabel("y values")
		plt.draw() #cant use plt.show() when we use a GUI. Will give an error called QCoreApplication exec event loop already running
		

#d=Polynomial(1, -0.2, -2, 2)
#d.plot_function()


