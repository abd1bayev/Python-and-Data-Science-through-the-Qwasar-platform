def my_string_index(param_1, param_2):
    if param_2 in param_1:
       return param_1.index(param_2)
    else:
        return -1

print(my_string_index("hello", "l"))
print(my_string_index("aaaaa", "b"))