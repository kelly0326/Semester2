# def unit_test():
# assert type(str_to_list('15,38,77')) == list, "error return is not a list"
# assert len(str_to_list('15,38,77')) == 3, f"error return list length should be 3, yours is {len(str_to_list('15, 38, 77'))}"
# 	assert str_to_list('15,38,77') == ['15', '38', '77'], f"{str_to_list('15,38,77')=}"
# 	assert strlist_to_intlist(['15', '38', '77']) == [15, 38, 77]
# 	assert sum_of_intlist([15, 38, 77]) == 130
# 	assert parse_article(['15, 38, 77', '1,1,1', '10,10,10']) == [130, 3, 30]
 


def get_column(data, column_number):
	"""
	Get a column from data2 (a list with strings)
	"""
	lst = []
	for row in data:
		lst.append(row[column_number])
	#print("lst", lst)
	return lst


def get_each_sum(data2):
	"""
	['15, 38, 77', '1,1,1', '10,10,10'] should return [130, 3, 30]

	"""
	sum_of_each_column = []
	for i in range(1, 6):
		lst = get_column(data2, i)
		count = strlist_to_intlist(lst)
		sum_column = sum_of_intlist(count)
		sum_of_each_column.append(sum_column) # float now

	sum_column_string = ["sum of each column"]
	for i in range(len(sum_of_each_column)):
		sum_of_each_column[i] = str(sum_of_each_column[i])
		sum_column_string.append(sum_of_each_column[i])
	#print("in 34", sum_column_string)
	return sum_column_string



def strlist_to_intlist(data): # float list
	"""
	['15', '38', '77'] should return [15, 38, 77]
	"""
	count = []
	for number in range(len(data)):
		if number != 0:
			data[number] = float(data[number])
			count.append(data[number])
	#print("in 26", count)
	return count



def sum_of_intlist(lst):
	"""
	[15, 38, 77] should return 130
	"""
	sum_column = sum(lst)
	#print("sum", sum_column)
	return sum_column



def read_file(path):
	file = open(path)
	data = file.read()
	#print(repr(data)) # string
	data1 = data.split("\n")
	#print(data1)

	data2 = []
	for row in data1:
		row = row.split(",")
		data2.append(row)
	#print(data2)
	return data2



def write_file(data, sum_column_string):
	file = open("my_new_file.csv", "w")
	for row in data:
		file.write(",".join(row))
		file.write("\n")
	file.write(",".join(sum_column_string))
	file.write("\n")



def main():
	data2 = read_file("amd_stock_data.csv")

	lst = get_column(data2, 3)

	count = strlist_to_intlist(lst)

	sum_column = sum_of_intlist(count)

	sum_column_string = get_each_sum(data2)

	write_file(data2, sum_column_string)



main()

# unit_test()