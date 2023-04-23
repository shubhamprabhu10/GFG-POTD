import math
class Solution:
    def minimumNumber(self,n, arr):
        g = arr[0]
        for i in range(1, n):
            g = math.gcd(g, arr[i])
        return g
