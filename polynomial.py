import numpy as np
#import matplotlib.pylab as plt
import matplotlib.pyplot as plt
from fractions import Fraction 
from function import *

class Polynomial(Function):
	def __init__(self, A, B, x_start, x_end):
		#print("got here")
		super().__init__(A, B, x_start, x_end)

	def x_range(self):
		#print("B is {}".format(self.B))
		#print("Denom is {}".format(Fraction(self.B).limit_denominator()))
		if (Fraction(self.B).limit_denominator().denominator % 2 == 0):
			self.x_start=0
		x_range = np.arange(self.x_start, self.x_end, 0.01)	
		#for i in range(len(x_range)):
		#	print("x value is {}".format(x_range[i]))
		#print("x start is {} and x end is {}".format(self.x_start, self.x_end))
		#print("denominator is {}".format(denom))
		if(self.B>0):
			#print("enter here 1")
			return x_range
		else:
			index=0
			for i in range(len(x_range)):
				if abs(x_range[i]) < 0.0001:
					index = i
					#print("number to remove is{}".format(x_range[index]))
					return np.delete(x_range, index)
			return x_range
	
	def y_values(self, x):
		#print("length of x {}".format(len(self.x_range())))
		fx=np.zeros(len(x))
		#x=self.x_range()
		for i in range(len(x)):
			#fx[i]=self.A*(x[i])**self.B
			#The following needs to be done because python cannot raise negative values to decimals that have an odd denominator. eg (-1)^0.2 or (-1)^-0.2 will not work 
			#print("Denom is {}".format(Fraction(self.B).limit_denominator().denominator))
			if Fraction(self.B).limit_denominator().denominator % 2 == 0 or Fraction(self.B).limit_denominator().denominator == 1 :
				fx[i]=self.A*(x[i])**self.B 
			else:
				fx[i]=self.A*(np.sign(x[i])*(np.abs(x[i]))**self.B)	
			#print("y values are {}, for x value {}".format(fx[i],x[i]))
		#print("length of y {}".format(len(fx)))
		return fx

	def plot_function(self):
		#print(np.amin(self.y_values()))
		#print(np.amax(self.y_values()))
		plt.close()
		plt.ion()
		plt.gcf().canvas.set_window_title('Polynomial function')
		plt.title("y=A*x^B, where A = {}, and B ={}".format(self.A, self.B))
		x = self.x_range()
		y = self.y_values(x)
		plt.ylim(np.amin(y)-1, np.amax(y)+1)
		plt.plot(x, y)
		plt.draw() #cant use plt.show() when we use a GUI. Will give an error called QCoreApplication exec event loop already running
		

#d=Polynomial(1, -0.2, -2, 2)
#d.plot_function()


