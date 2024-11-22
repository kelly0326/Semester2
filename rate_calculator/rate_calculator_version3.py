INTEREST_RATE = 0.035 # global constant (all constant should be all in capital)

withdraw = 0
year = 0
deposit = 0

while True:
	print("===menu===")
	print("d) input your deposit")
	print("y) input your duration")
	print("p) display your future balance")
	print("a) analyze your balance")
	print("w) withdraw money")
	print("q) quit")

	command = input("please select the menu: ")
	if command == "q":
		print("goodbye")
		break
	if command == "d":
		while True:
			deposit = input("how much is your deposit? ")
			if deposit.replace(".", "").isdigit():
				deposit = float(deposit)
				break
			else:
				print("deposit must be positive integer or float.")

	if command == "y":
		while True:
			year = input("how long do you want to deposit? ")
			if year.isdigit():
				year = int(year)
				break
			else:
				print("year must be positive integer.")
	if command == "w":
		while True:
			withdraw = input("how much is your withdraw per year? ")
			if withdraw.replace(".", "").isdigit():
				withdraw = float(withdraw)
				break
			else:
				print("withdraw must be positive integer or float.")

	if command == "p":
		balance = deposit
		for i in range(year):
			if balance - withdraw >= 0:			
				balance = balance * (1 + INTEREST_RATE) - withdraw
				print(f"year {i + 1:>2d}: your balance is ${balance:,.2f}")
			else:
				print("balance is not enough for withdraw:", balance)
				break

	if command == "a":	
		balance = deposit
		count = 0
		while balance < deposit * 2:
			balance = balance * (1 + INTEREST_RATE)
			count = count + 1
		print("-" * 50)
		print("it will take", count, "years to double the deposit.")
		print("after that, deposit will be: ", balance)
		print("-" * 50)