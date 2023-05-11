class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        # code here
        if(0 not in arr):
            return 1
        ch=[0]*n
        if(ch==arr):
            return 0
        c=0
        posn=-10
        if(arr[0]==0):
            posn=0
        for i in range(n):
            if(arr[i]==0 and (i-1)!=posn):
                c=c+1
                posn=i
        if(arr[0]!=0 and arr[-1]!=0):
            c=c+1
        if(arr[0]==0 and arr[-1]==0):
            c=c-1
        return c
