class Solution:
    def reverseEqn(self, s):
        # code here
        op=['+','-','*','/']
        l=len(s)
        ans=""
        n=""
        for i in range(l-1,-1,-1):
            if(s[i] not in op):
                n=s[i]+n
            else:
                ans=ans+n+s[i]
                n=""
        ans=ans+n
        return(ans)
