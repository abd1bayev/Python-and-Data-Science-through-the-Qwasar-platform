def count_vowels_permutation(param_1):

    dp = [[0] * 5 for i in range(param_1)]

    dp[0] = [1] * 5

    for i in range(1, param_1):
        dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
        dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
        dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
        dp[i][3] = dp[i - 1][2]
        dp[i][4] = dp[i - 1][2] + dp[i - 1][3]

    return sum(dp[-1]) % (10 ** 9 + 7)

print(count_vowels_permutation(4))