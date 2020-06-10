import numpy as np
import matplotlib.pylab as plt
from function import *

class trig(Function):
	def __init__(self, A, B, x_start, x_end):
		super().__init__(A, B, x_start, x_end)
	
	def x_range(self):
		super().x_range()

	def y_values(self):
		return self.A * np.sin(self.B*(super().x_range()))

	def plot_function(self):
		plt.close()
		plt.ion()
		plt.gcf().canvas.set_window_title('Trigonometric function')
		plt.title("y=A*sin(Bx), where A = {}, and B ={}".format(self.A, self.B))
		plt.plot(super().x_range(), self.y_values())
		plt.draw()

#d=trig(2, 100, 0, 5)
#d.plot_function()
