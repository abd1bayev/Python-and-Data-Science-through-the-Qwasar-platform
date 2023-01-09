def my_iterative_factorial(param_1):
	a = 1
	for i in range(1, param_1 +1):
		a*=i
	return a

print(my_iterative_factorial(6))