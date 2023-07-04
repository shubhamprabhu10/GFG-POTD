class Solution:
    def countSubArrayProductLessThanK(self,a,n,k):
        i = 0
        j = 0
        pro = 1
        ans = 0
        while i < n:
            pro *= a[i]
            while j <= i and pro >= k:
                pro /= a[j]
                j += 1
            ans += (i - j + 1)
            i += 1
        return ans
