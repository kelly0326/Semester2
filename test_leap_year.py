# test code
from leap_year import *

def test_is_leap():
	assert is_leap(1996) == True
	print("1996 passed.")
	assert is_leap(1997) == False
	print("1997 passed.")
	assert is_leap(2000) == True
	print("2000 passed.")
	
	print(f"{is_leap(1900)=}")
	assert is_leap(1900) == False
	print("1900 passed.")
	print("=" * 35)
	print("test is leap, all passed.")

test_is_leap()