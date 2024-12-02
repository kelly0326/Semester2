def plus(a, b):
	print("in function", a + b)
	return (a + b)
print(plus(3, 5)) # 8 (why not 'in function', 8?)
plus(10, 20)
print("program runs successfully.")




def test(a, b, c):
	return (a + b + c)

test(1, 5, 2.5)

result = test(1, 5, 2.5)
print(result)


print("==================")
def test(a, b):
	return (a * b)

print(test(3, 9))