def is_power_of_(num):
    num = (num and (not num & (num-1)) & (num != 1))
    return 1 if num else 0

print(is_power_of_(4))