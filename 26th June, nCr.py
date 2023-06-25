import math
class Solution:
    def nCr(self, n, r):
        nu=math.factorial(n)
        rf=math.factorial(r)
        c=n-r
        if(c>0 and n>0 and r>0):
            d=math.factorial(c)
            m=rf*d
            ans=nu//m
        elif(n==r):
            ans=1
        else:
            ans=0
        return int(ans%(10**9+7))
