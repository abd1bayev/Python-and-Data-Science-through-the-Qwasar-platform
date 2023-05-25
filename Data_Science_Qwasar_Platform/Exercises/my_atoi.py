
def my_atoi(param_1):
    if not param_1:
        return 0

    result = 0
    sign = 1
    i = 0

    # Handling leading whitespace
    while i < len(param_1) and param_1[i].isspace():
        i += 1

    # Handling sign
    if i < len(param_1) and (param_1[i] == '+' or param_1[i] == '-'):
        sign = -1 if param_1[i] == '-' else 1
        i += 1

    # Converting string to integer
    while i < len(param_1) and param_1[i].isdigit():
        result = (result * 10) + int(param_1[i])
        i += 1

    return sign * result