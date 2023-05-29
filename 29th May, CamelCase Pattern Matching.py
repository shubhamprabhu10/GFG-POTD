class Solution:
    def CamelCase(self,N,d,p):
        #code here
        def s(n):
            l=''
            for j in range(len(n)):
                if n[j].isupper():l += str(n[j])
            return l
        m=[]
        for i in range(N):
            l=s(d[i])
            k=0
            if p in l[:len(p)]:
                m.append(d[i])
        if len(m)==0:
            m.append(-1)
        return m
