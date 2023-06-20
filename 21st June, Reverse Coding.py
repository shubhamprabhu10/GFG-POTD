class Solution:
    def sumOfNaturals(self, n):
        m=1000000007
        return (((n*(n+1))%m)//2)
