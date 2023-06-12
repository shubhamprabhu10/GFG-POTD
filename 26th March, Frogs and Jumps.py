class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # code here
        l=[0]*leaves
        if 1 in frogs:
            return 0
        c=0
        frogs.sort()
        for i in frogs:
            if(i>leaves or l[i-1]==1):
                continue
            for j in range(i-1,leaves,i):
                l[j]=1
                # print("bruh")
        # print(l)
        for y in l:
            if(y==0):
                c=c+1
        return c
