def encoding(original, code):
	"""
	Description: This function takes a original string, and a code number
	then returns an encoded string
	Parameters: original (str)
				code (int)
	Returns: str
	"""
	encoded = ""
	for ch in original:
		asc_no = ord(ch) # a will return 97
		asc_no += code # 97 + 1 = 98
		new_character = chr(asc_no) # chr (98) returns b
		encoded += new_character
		print(ch, "=>", new_character)
		print(encoded)

def advanced_encoding(original, code):
	"""
	Description: This function takes a original string, and a code number
	then returns an encoded string, compare with encoding function, this
	function also handle out of range issues
	Parameters: original (str)
				code (int)
	Returns: str
	"""
	encoded = ""
	for ch in original:
		asc_no = ord(ch) # a will return 97
		asc_no += code % 25 # 97 + 1 = 98
		new_character = chr(asc_no) # chr (98) returns b
		encoded += new_character
		print(ch, "=>", new_character)
		print(encoded)

def unit_test():
	assert encoding("abcd", 1) == "bcde", "abcd doesn't return a correct value"
# unit_test()
advanced_encoding("aaaa", 26)