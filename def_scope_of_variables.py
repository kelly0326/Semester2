# def & scope of variables
def plus5(x):
	return x + 5

plus5(100)
# 105


# Calculate x^2 + 5x + 100
def polynominal(x):
	return x **2 + 5 * x + 100

polynominal(0)
# 100
polynominal(-1)
# 96

# Scope of variables

# global variable
lst = list(range(-10, 11))
lst
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
for num in lst:
    total += num
total
# 0

def my_total(sourced_lst): # global
    # all variables below is local variable
    total = 0
    for num in sourced_lst:
        total += num
    return total

 my_total([1, 2])
 # 3