def reverse_integer(x):
    if x > (-2 ** 31) and x < ((2 ** 31) - 1):
        y = x
        x = str(x)
        if y < 0:
            x = ('-' + x[::-1])
            x = x[:-1]
            x = int(x)
            if x > (-2 ** 31) and x < ((2 ** 31) - 1):
                return x
            else:
                return 0
        else:
            x = x[::-1]
            x = int(x)
            if x > (-2 ** 31) and x < ((2 ** 31) - 1):
                return x
            else:
                return 0
    else:
        return 0

print(reverse_integer(123))