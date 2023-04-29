class Solution:
    def findNumber(self, N : int) -> int:
        # code here
        arr=[9,1,3,5,7]
        curr=1
        ans=0
        while N>0:
            ans=arr[N%5]*curr+ans
            if N%5==0:
                N=int(N/5)-1
            else:
                N=int(N/5)
            curr=curr*10

        return ans
