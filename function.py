"""
This abstract class contains methods that all functions should have. 
All functions should extend this abstract class
If a new function class is added, it should extend this abstract class
"""

from abc import ABC, abstractmethod
import numpy as np

class Function(ABC):
	def __init__(self, A, B, x_start, x_end):
		self.A=A
		self.B=B
		self.x_start=x_start
		self.x_end=x_end
		
	@abstractmethod
	def x_range(self):
		return np.arange(self.x_start, self.x_end, abs((0.2/self.B))) #(start val, end val, step size)

	@abstractmethod
	def y_values(self):
		pass

	@abstractmethod	
	def plot_function(self):
		pass
