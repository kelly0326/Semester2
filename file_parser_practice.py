'''
Author: Shu Liu
Date: 2024/12/10
Version: 1.0.0
License: MIT
'''
def read_data():
	"""
    Description:
        This function takes file name as path, `open`the file
        `read`the file and save it in the variable `data`
        Use `split('\\n')` and `split(",")` convert data to a nested list
        Then return the list
    Return: lst
    Precondition: data must be a 2D list, column_number must be an integar
                  smaller than the length of the first row
    """
	file = open("amd.csv")
	data = file.read()
	print("data type:", type(data)) # string (raw data)
	print(repr(data))

	# convert data (string) to data1 (list)
	data1 = data.split("\n")
	print(data1)
	print("data1 type:", type(data1)) # list

	# convert data1 (list) to a nested list: data2.
	data2 = []
	for temp in data1:
		temp = temp.split(",")
		data2.append(temp)

	print("data2 type:", type(data2)) # nested list
	print(data2)
	return data2


# use the previous nested list (data2) to retrieve the column
def get_column(data, column_number):
	"""
    Description:
        This function takes two parameters data and column_number
        and `append` the elements into a new empty list(lst).
    Parameter: data, column_number
    Return: lst
    Precondition: data must be a 2D list, column_number must be an integar
                  smaller than the length of the first row
    """
	lst = []
	for row in data:
		lst.append(row[column_number])
	print("in 29", lst)
	return lst


# convert the column (my_column) to float
def float_column(my_column):
	count = []
	for number in range(len(my_column)):
		if number != 0:
			my_column[number] = float(my_column[number])
			count.append(my_column[number])
	print("in line 38", count)
	return count


# print average
def average(my_float_column):
	average = sum(my_float_column) / len(my_float_column)
	return average


	

#
def write_file(data):
	print(data)
	avg = ["avg="]
	for i in range(1, 6):		
		temp = get_column(data, i)
		print("in 61", temp)
		temp = float_column(temp)
		print("in 63", temp)
		avg1 = average(temp)
		print(avg1)
		avg.append(str(avg1))
	print(avg)
	data.append(avg)
	print(data)
	for row in data:
		print(row)
	file = open("new_amd.csv", "a") # a: append r: read w: write
	#file.write("hello world.")
	#file.write("hello again.")
	for row in data:
		file.write(",".join(row)) # .join() must to be used by string (here, row must be string)
		file.write("\n") # Enter


def main():
	# call read_data() to return data2 (a nested list)
	data2 = read_data()

	# get the column by using the previous data (data2) to retrieve
	my_column = get_column(data2, 4)
	print("in line 48", my_column)

	# convert the column from string to float
	my_float_column = float_column(my_column)
	print("in 60", my_float_column)

	# print average value
	avg = average(my_float_column)
	print(f"{avg=:.2f}")

	write_file(data2)

main()