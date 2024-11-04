# My_List

lst7 = [100,2,5,8,9,11,15]
lst8 = [10,10,20,11,12,15,14,188,201]
lst9 = []

if len(lst7) >= len(lst8):
	max_length = len(lst7)
else:
	max_length = len(lst8)

while len(lst7) != len(lst8):
	if max_length == len(lst7):
		lst8.append(0)
	elif max_length == len(lst8):
		lst7.append(0)
	else:
		break

print(lst7)
print(lst8)

for i in range(len(lst7)):
	lst9.append(lst7[i] + lst8[i])

lst9