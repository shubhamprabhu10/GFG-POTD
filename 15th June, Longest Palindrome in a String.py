class Solution:
    def longestPalin(self, s: str):
        def lp(s,l,r):
            n=len(s)
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return l+1,r
        start=end=0
        for i in range(len(s)):
            l,r=lp(s,i,i)
            if (r-l)>(end-start):
                start=l
                end=r
            l,r=lp(s,i,i+1)
            if (r-l)>(end-start):
                start=l
                end=r
        return s[start:end]
