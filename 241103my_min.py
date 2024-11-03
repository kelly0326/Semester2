lst = [-2,-5,-8,-7]
my_min = float("inf")
for num in lst:
	if num < my_min:
		my_min = num
	       # -2
	       # -5
	       # -8
print("list: ", lst)
print("The minimum of this list is: ", my_min)
