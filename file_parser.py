'''
Author: Shu Liu
Date: 2024/12/10
Version: 1.0.0
License: MIT
'''
# Above all belong to 'file level doc string'

# below all belong to 'function level doc string'
def convert_type(lst):
	''' # Doc string
	Description: 
		This function takes a Python string list, and convert to the 
		correct data type.
	Parameter: lst(list)
	Return: (list)
	Precondition: lst must be a python list, data type is string. # law regulated
	'''

# (Precondition is most important. You cannot miss it at work!)

def get_column(data, column_number):
	pass

def read_data(path):
	"""
	Description:
		This function takes file name as path, `open`the file
		`read`the file and save it in the variable `data`
		Use `split('\\n')` and `split(",")` convert data to a nested list
		Then return the list
	Parameter: path(str)
	Return: (2d list)
	Precondition: 
		File must in the same folder with Python script, file name must correct
	"""
	file = open(path)

def main():
	# call read_data to get the 2d list


	# use the previous data and get_column to retrieve the column

	# convert the column to float

	print("System exit successfully.")