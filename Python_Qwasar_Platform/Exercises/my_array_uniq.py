def my_array_uniq(param_1):
    j = []
    for a in param_1:
        if a not in j:
            j.append(a)
    return j

print(my_array_uniq([1, 1, 1, 2, 3, 4, 1]))