def my_count_on_it(param_1):
    j = []
    for a in param_1:
        b = len(a)
        j.append(b)
    return j

print(my_count_on_it(["This", "is", "the", "way"]))