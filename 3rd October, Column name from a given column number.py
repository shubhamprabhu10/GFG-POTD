class Solution:
    def colName (self, n):        
        ans=""
        while n:
            n=n-1
            r=n%26
            n=n//26
            ans=chr(ord("A")+r)+ans
        return ans
