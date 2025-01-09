# productive code (turn it in to the boss after done with the code)
def is_leap(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0: # 1900 / 4 = 475
		return True
	else:
		return False

