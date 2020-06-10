"""
Add custom exceptions if required
"""
class xRangeError(Exception):
	"""
	If the user enters an x_end value that is not greater than 
	x_start value, then xRangeError exception is raised
	"""
	pass

class emptyBoxError(Exception):
	"""
	If any of the input fields are left empty, notify the user
	"""
	pass