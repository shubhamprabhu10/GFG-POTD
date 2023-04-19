class Solution:
    def wifiRange(self, N, S, X): 
        res = [i for i in range(N) if S.startswith("1", i)]
        # print(res)
        s1=S[0:res[0]]
        s2=S[res[len(res)-1]+1:N]
        if(len(s1)>X or len(s2)>X):
            return 0
        for i in range(0,len(res)-1):
            a=res[i]
            b=res[i+1]
            c=abs(b-a)
            # print(a,end=" ")
            # print(b)
            if((c-1)>(2*X)):
                return 0
        return 1
