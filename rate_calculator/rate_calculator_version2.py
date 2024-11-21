INTEREST_RATE = 0.035 # global constant (all constant should be all in capital)

while True:
	deposit = input("how much is your deposit? ")
	if deposit.replace(".", "").isdigit():
		deposit = float(deposit)
		break
	else:
		print("deposit must be positive integer or float.")

while True:
	year = input("how long do you want to deposit? ")
	if year.isdigit():
		year = int(year)
		break
	else:
		print("year must be positive integer.")


balance = deposit
for i in range(year):
	balance = balance * (1 + INTEREST_RATE)
	print(f"year {i + 1:>2d}: your balance is ${balance:,.2f}")

balance = deposit
count = 0
while balance < deposit * 2:
	balance = balance * (1 + INTEREST_RATE)
	count = count + 1
print("-" * 50)
print("it will take", count, "years to double the deposit.")
print("after that, deposit will be: ", balance)
print("-" * 50)