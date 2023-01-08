def my_isalpha(param_1):
	harf = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
	for i in harf:
		if i == param_1:
			return 1
	else:
		return 0

print(my_isalpha("s"))