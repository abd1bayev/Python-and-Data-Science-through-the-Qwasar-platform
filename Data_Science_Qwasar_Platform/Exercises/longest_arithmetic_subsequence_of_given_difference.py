def longest_arithmetic_subsequence_of_given_difference( arr, diff):
    res = {}
    for num in arr:
        res[num] = res[num - diff] + 1 if (num - diff) in res else 1
    return max(res.values())

print(longest_arithmetic_subsequence_of_given_difference([1,2,3,4],1 ))