from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pylab as plt

class Function(ABC):

	def __init__(self, A, B, x_start, x_end):
		self.A=A
		self.B=B
		self.x_start=x_start
		self.x_end=x_end

		
	@abstractmethod
	def x_range(self):
		x_range = np.arange(self.x_start, self.x_end, abs((0.2/self.B)))
		#size=len(x_range)
		#print(len(x_range))
		#if self.B < 0:
		#	for i in range(size):
		#		if abs(x_range[i]-0)<0.001:
		#		print(x_range[i])
		#	return x_range
		return x_range

	@abstractmethod
	def y_values(self):
		pass

	@abstractmethod	
	def plot_function(self):
		pass
#Stuff to handle:
#start and end range cannot be same 