deposit = input("how much is your deposit? ")
deposit = float(deposit)

interest_rate = 3.5 / 100
year = input("how long do you want to deposit? ")
year = int(year)
print(deposit, year)

balance = deposit
for i in range(year):
	balance = balance * (1 + interest_rate)
	print(f"year {i + 1:>2d}: your balance is ${balance:,.2f}")

balance = deposit
count = 0
while balance < deposit * 2:
	balance = balance * (1 + interest_rate)
	count = count + 1
print("-" * 50)
print("it will take", count, "years to double the deposit.")
print("after that, deposit will be: ", balance)
print("-" * 50)