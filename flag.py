# nested for loop

def test(row, column):
	for i in range(row):
		for j in range(column):
			print("*", end = "") # j loop run first
		print() # like ENTER function

# test(5, 11)


def flag1():
	for i in range(13):
		print(i, end = "")
		for j in range(39):
			print("*", end = "")
		print("|") # the row ending



def flag2():
	for i in range(13):
		print("|", end = "")
		for j in range(39):
		#	print("*", end = "")
			if i % 2 == 0:
				print("0", end = "")
			else:
				print("1", end = "")
		print("|") # the row ending
# flag2()



def flag3():
	for i in range(13):
		print("|", end = "")
		for j in range(39):
			if i < 9 and j <= 12:
				print("*", end = "")
			else:
				if i % 2 == 0:
					print("0", end = "")
				else:
					print("1", end = "")
		print("|") # the row ending
# flag3()


def flag4():
	for i in range(13):
		print("|", end = "")
		for j in range(39):
			# this is * area
			if i < 9 and j < 12:
				# this is the even row
				if i % 2 == 0 and j % 2 == 0:
					print("*", end = "")
				# this is odd row determined by i
				elif i % 2 == 1 and j % 2 == 1 and j !=
					print("*", end = "")
				else: # this is all spaces
					print(" ", end = "")
			# this is stripe area
			else:
				if i % 2 == 0:
					print("0", end = "")
				else:
					print("1", end = "")
		print("|") # the row ending
flag4()