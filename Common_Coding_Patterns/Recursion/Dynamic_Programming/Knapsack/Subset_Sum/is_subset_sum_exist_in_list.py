def is_subset_sum_exist_in_list(arr, total):
    N = len(arr)
    M = total + 1
    dp = [[-1 for j in range(M)] for i in range(N + 1)]

    for i in range(1, M):
        dp[0][i] = False

    for j in range(N):
        dp[j][0] = True

    for i in range(1, N):
        for j in range(1, M):
           dp[i][j] = dp[i - 1][j]
           if arr[i - 1] <= j:
               dp[i][j] |= dp[i - 1][j - arr[i]]

    return dp[N - 1][M - 1]


print(is_subset_sum_exist_in_list([2, 3, 7, 8, 10], 11))