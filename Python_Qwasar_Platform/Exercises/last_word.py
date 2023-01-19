def last_word(param_1):
	if param_1 !="":
		param_1 = param_1.replace("," , " " )
		word = param_1.split()
		return word[len(word)-1]
	else:
		return ""

print(last_word("this        ...       is sparta"))