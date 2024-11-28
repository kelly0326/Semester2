INTEREST_RATE = 0.035

def menu():
    print("==============menu=================")
    print("a) how much is your deposit?")
    print("b) how long do you want to deposit?")
    print("c) display your future balance")
    print("d) analyze your balance")
    print("e) how much is your withdraw per year?")
    print("q) quit")

def deposit(): # global variable
    while True:
        deposit = input("how much is your deposit?")
        if deposit.isdigit():
            deposit = int(deposit)
            return deposit
            break
        else:
            print("your deposit must be a positive integer.")

def duration():
    while True:
        year = input("how long do you deposit?")
        if year.isdigit():
            year = int(year)
            return year
            break
        else:
            print("year must be a positive integer.")

def display(deposit = 0, year=0, withdraw=0):
    # the argument without a value is called 'positional argument'
    # the argument with a value is called 'keyword argument'
    # the only rule is positional must before keyword (deposit is positional here)
    balance = deposit
    count = 0
    for i in range(year):
        if balance - withdraw > 0:
            balance = balance * (1 + INTEREST_RATE) - withdraw
            count = count + 1
            print(f"year {count:>2d}: ${balance:.2f}")
        else:
            print("balance is not enough for withdraw:", balance)
            break

def analyze(deposit):
    balance = deposit
    count = 0
    while True:
        if balance == 0:
            break
        if balance <= deposit * 2:
            balance = balance * (1 + INTEREST_RATE)
            count = count + 1
        else:
            break
    print(f"It will take {count} years for your deposit to be doubled. After that, your balance will be ${balance:.2f}.")

def withdraw():
    while True:
        withdraw = input("how much do you withdraw per year?")
        if withdraw.isdigit():
            withdraw = int(withdraw)
            return withdraw
            break
        else:
            print("your withdraw must be a positive integer.")

def main():
    customer_deposit = 0
    year = 0
    customer_withdraw = 0

    while True:
       # menu()
        command = input("please select the menu:")
        if command == "a":
            customer_deposit = deposit()
        if command == "b":
            year = duration()
        if command == "c":
            display(customer_deposit, year, customer_withdraw)
        if command == "d":
            analyze(customer_deposit)
        if command == "e":
            customer_withdraw = withdraw()
        if command == "q":
            print("thank you for using.")
            break

main() # 1st function call