def find_k_closest_elements(param_1, param_2, param_3):
    if param_1[0] > param_3:
        return param_1[:param_2]
    elif param_1[-1] < param_3:
        return param_1[-param_2:]
    else:
        n = len(param_1) - param_2
        low = 0
        high = len(param_1) - 1
        while n != 0:
            if abs(param_1[low] - param_3) <= abs(param_1[high] - param_3):
                high -= 1
            else:
                low += 1
            n -= 1
        return param_1[low:high + 1]

print(find_k_closest_elements([1,2,3,4,5], 4, 3 ))