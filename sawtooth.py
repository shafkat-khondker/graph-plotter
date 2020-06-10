"""
The SawTooth function does not have a simple mathmetical representation 
It is a asymmetrical triangle, with an upward slope of 1, downward slope of -0.5, and a width of 3 x units 
"""
import numpy as np
import matplotlib.pyplot as plt
from function import *

class SawTooth(Function):
	
	def __init__(self, A, B, x_start, x_end):
		self.y_vals=[]
		super().__init__(A, B, x_start, x_end)

	def x_range(self):
		#for the sawtooth graph, the input values of x range is converted to integers for simplify calculations
		return np.arange(int(self.x_start), int(self.x_end)+1, 1)

	def y_values(self):
		return self.y_vals

	def plot_function(self):
		x=self.x_range()
		y=self.y_values()
		i=0
		x_first=int(self.x_start)
		while i<len(x+1):
			if x_first % 3 is 0: #the upward slope only begins for values of x that is divisible by 3
				self.up_slope(x[i])
				x_first+=1
				i+=1
			else:
				self.down_slope(x[i])
				x_first+=1
				i+=1
		
		plt.close()
		plt.ion()
		plt.gcf().canvas.set_window_title('Sawtooth function')
		plt.title("Scaling factor A = {}, and Vertical shift B ={}".format(self.A, self.B))
		plt.plot(x, y)
		plt.xlabel("x values")
		plt.ylabel("y values")
		plt.show()

	def down_slope(self, x_value):
		#calculates the y values for the downward slope
		self.y_values().append((1-0.5*(x_value % 3))*self.A + self.B)

	def up_slope(self, x_value):
		#calculates the y values for the upward slope
		self.y_values().append(((x_value % 3)-0.5)*self.A + self.B)


#d=SawTooth(4, 4, -5, 5)
#d.plot_function()

