class Solution:
    def cutRod(self, price, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            temp = float('-inf')
            for j in range(i):
                temp = max(temp, price[j] + dp[i - j - 1])
            dp[i] = temp
        return dp[n]
