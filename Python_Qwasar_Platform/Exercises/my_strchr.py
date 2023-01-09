def my_strchr(param_1, param_2):
	for i in range(len(param_1)):
		if param_1[i]==param_2:
			return param_1[i:]

print(my_strchr("abcabc", "b"))