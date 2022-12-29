def alpha_mirror(param_1):
	a = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA ."
	b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ."
	res = ""

	for i in param_1:
		if i in a:
			index = a.index(i)
			res += b[index]
	return (res)

print(alpha_mirror("My horse is Amazing."))