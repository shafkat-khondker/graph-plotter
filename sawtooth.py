import numpy as np
import matplotlib.pyplot as plt
from function import *

class SawTooth(Function):
	
	def __init__(self, A, B, x_start, x_end):
		self.y_vals=[]
		super().__init__(A, B, x_start, x_end)


	def x_range(self):
		return np.arange(int(self.x_start), int(self.x_end)+1, 1)

	def y_values(self):
		return self.y_vals

	def plot_function(self):
		x=self.x_range()
		y=self.y_values()
		i=0
		x_first=int(self.x_start)
		while i<len(x+1):
		#	print("x start modulus {}".format(x_first % 3))
			if x_first % 3 is 0:
				self.up_slope(x[i])
				x_first+=1
				i+=1
			else:
				self.down_slope(x[i])
				x_first+=1
				i+=1
		#for x in range(len(self.x_range())):
		#	print(self.x_range()[x])
		#print("length of x is {}".format(len(self.x_range())))
		#print("length of y is {}".format(len(self.y_values())))
		plt.close()
		plt.ion()
		plt.gcf().canvas.set_window_title('Sawtooth function')
		plt.title("Scaling factor A = {}, and Vertical shift B ={}".format(self.A, self.B))
		plt.plot(x, y)
		plt.xlabel("x values")
		plt.ylabel("y values")
		plt.show()

	def down_slope(self, x_value):
		self.y_values().append((1-0.5*(x_value % 3))*self.A + self.B)

	def up_slope(self, x_value):
		self.y_values().append(((x_value % 3)-0.5)*self.A + self.B)


#d=SawTooth(4, 4, -5, 5)
#d.plot_function()

