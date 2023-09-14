class Solution:
    def perfectSum(self, arr, n, sum):
        # code here
        MOD = 1000000007
        arr = list(filter(lambda x : x <= sum, arr))
        n = len(arr)
        dp = [[0 for _ in range(sum + 2)] for __ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):  
            for j in range(sum + 1):
                if j >= arr[i]:
                    dp[i + 1][j] = (dp[i][j] + dp[i][j - arr[i]]) % MOD
                else:
                    dp[i + 1][j] = dp[i][j]
        return dp[n][sum]
