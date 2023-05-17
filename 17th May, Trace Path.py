class Solution:
    def isPossible(self, n, m, s):
        l=r=u=d=0
        lr=0
        ud=0
        for i in s:
            if i=='L':
                lr-=1
                if lr<l:
                    l=lr
            if i=='R':
                lr+=1
                if lr>r:
                    r=lr
            if i=='U':
                ud+=1
                if ud>u:
                    u=ud
            if i=='D':
                ud-=1
                if ud<d:
                    d=ud
        
        if r-l+1>m or u-d+1>n:
            return 0
        else:
            return 1
