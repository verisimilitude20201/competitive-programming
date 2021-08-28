def are_subsets_with_same_sum_present(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False

    actual_sum = int(total / 2)
    dp = [[None for j in range(actual_sum + 1)] for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(actual_sum + 1):
            # If sum is 0, there can be empty subset
            dp[i][0] = True
            # If number of elements are 0, no subsets possible
            if j + 1 > actual_sum:
                break
            dp[0][j+1] = False

    for i in range(1, len(arr)):
        for j in range(1, actual_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i] <= j:
                dp[i][j] |= dp[i-1][j - arr[i]]

    return dp[len(arr) - 1][actual_sum]


print(are_subsets_with_same_sum_present([1, 5, 5, 11]))