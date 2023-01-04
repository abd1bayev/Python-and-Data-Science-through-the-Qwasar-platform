def count_of_range_sum( param_1, param_2, param_3):
    count_sum = {0: 1}

    pre_sum = 0
    count = 0

    for num in param_1:
        pre_sum += num

        for d in range(param_2, param_3 + 1):
            if pre_sum - d in count_sum:
                count += count_sum[pre_sum - d]

        count_sum[pre_sum] = count_sum.get(pre_sum, 0) + 1

    return count

print(count_of_range_sum([-2,5,-1],-2,2))