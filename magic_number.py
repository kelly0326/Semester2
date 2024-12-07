import time
def triple_digit_test():
	for i in range(0, 4):
		for j in range(0, 4): #
			for k in range(0, 4): # run first (from 0 to 3)
				print(f"{i=}, {j=}, {k=}")
# triple_digit_test()


def clock():
	for i in range(0, 10):
		for j in range(0, 6):
			for k in range(0, 10):
				print(f"{i} : {j}{k}")
				time.sleep(1)

# clock()

def clock_optimized():
	for minute in range(60):
		for second in range(60):
			print(f"{str(minute).zfill(2)}: {str(second).zfill(2)}")
			time.sleep(0.2)
clock_optimized()


def triple_digit():
	for i in range(0, 10):
		for j in range(0, 10):
			for k in range(0, 10):
				if i + j + k == i * j * k:
					print(i * 100 + j * 10 + k)
# triple_digit()


def five_digit():
	for i in range(10):
		for j in range(10):
			for k in range(10):
				for l in range(10):
					for m in range(10):
						if i + j + k + l +m == i * j * k * l * m:
							print(i * 10000 + j * 1000 + k * 100 + l * 10 + m)
# five_digit()