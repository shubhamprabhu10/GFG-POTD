class Solution:
    def leastPrimeFactor(self,n):
        ans = [0] * (n+1)
        ans[1] = 1
        for i in range(2, n+1):
            if ans[i] == 0:
                ans[i] = i
                for j in range(2*i, n+1, i):
                    if ans[j] == 0:
                        ans[j] = i
        return ans
