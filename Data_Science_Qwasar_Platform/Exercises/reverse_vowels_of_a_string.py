def reverse_vowels_of_a_string(param_1):
	a = ""
	for b in param_1:
		if b in "aeiouAEIOU":
			a += b
	str = ""
	for b in param_1:
		if b in "aeiouAEIOU":
			str += a[-1]
			a = a[:-1]
		else:
			str += b
	return str

print(reverse_vowels_of_a_string("hello"))