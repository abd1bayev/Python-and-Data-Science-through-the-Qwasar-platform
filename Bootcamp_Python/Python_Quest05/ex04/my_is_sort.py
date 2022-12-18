def my_is_sort(param_1):
    if param_1== sorted(param_1) or param_1== sorted(param_1,reverse= True):
        return True
    else:
        return False

print(my_is_sort([2, 1, -1]))
print(my_is_sort([4, 7, 0, 3]))
