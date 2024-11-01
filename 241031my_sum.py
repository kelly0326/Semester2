list_ = [25,10,1,1,1,2,30]
# define a initializor 
my_sum = 0
# update this initializor multiple times
for num in list_:
	my_sum = my_sum + num
		   #    0      25
		   #    25     10
		   #    35      1
print("list: ", list_)
print("my sum of this list is: ", my_sum)