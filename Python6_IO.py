Python6_IO

deposit = input("how much is your deposit?")
# 520
deposit = int(deposit)
rate = input("how much is the interest rate?")
# 3.5
rate = float(rate)
rate = rate / 100
rate
# 0.035
year = input("how many years do you want to deposit?")
year = int(year)

# How many years can the deposit be doubled? (deposit = 520) 520 * 2 = 1040a
# Method 1
balance = deposit
count = 0
while balance <= deposit * 2:
    balance = balance * (1 + rate)
    count = count + 1
    print(count, balance)
    

# Method 2
balance = deposit
count = 0
while True:
    balance = balance * (1 + rate)
    count = count + 1
    print(count, balance)
    if balance >= deposit * 2:
        break


while True:
    value = input("must input a positive integer:")
    if value.isdigit():
        value = int(value)
        break
    else:
        print("your value", value, "is not a positive integer")


while True:
    value = input("must input a positive integer")
    if value.count(".") != 0:
        print(value, "is a float not an integer")
    elif value.isdigit():
        value = int(value)
        break
    else:
        print("your value:", value, "is not a positive number")