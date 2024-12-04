def plus(a, b):
	print("in function", a + b)
	return (a + b)

print(plus(3, 5)) # in function 8 
				  # 8
plus(10, 20) # in function 30
print("program runs successfully.") # program runs successfully.




def test(a, b, c):
	return (a + b + c)

test(1, 5, 2.5) # nothing in terminal to print out

result = test(1, 5, 2.5)
print(result) # 8.5


print("==================") # ==================

def test(a, b):
	return (a * b)

print(test(3, 9)) # 27